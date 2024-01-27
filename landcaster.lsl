// landcaster
// JR 20240119

integer Tests;
integer Correct;
integer Errors;
key Query;
string URL;

run_tests() {
    Tests = 0;
    Correct = 0;
    Errors = 0;
    test_int2hex();
    llOwnerSay((string)Tests + " Tests " + (string) Correct + " Correct " + (string) Errors + " Errors");
}

assertEqualsSS(string actual, string expected) {
    Tests++;
    if (actual != expected) {
        llOwnerSay(actual + " != " + expected);
        Errors++;
    } else {
        // llOwnerSay("OK " + actual + " == " + expected);
        Correct++;
    }
}

test_int2hex() {
    assertEqualsSS(int2hex(0), "00");
    assertEqualsSS(int2hex(33), "21");
    // assertEqualsSS(int2hex(33), "24"); // error
    assertEqualsSS(int2hex(255), "FF");
}

string Hex = "0123456789ABCDEF";

string int2hex(integer x) {
    string char1 = llGetSubString(Hex, x/16, x/16);
    string char2 = llGetSubString(Hex, x%16, x%16);
    return char1+char2;
}

string scan(integer x, integer y, integer z) {
    vector start = <x, y, z>;
    vector end = <x, y, 0>;
    list params = [RC_REJECT_TYPES, RC_REJECT_AGENTS, RC_DETECT_PHANTOM, TRUE];
    list result = llCastRay(start, end, params);
    integer status = llList2Integer(result, -1);
    if (status  < 0 ) {
        return "???";
    } else {
        vector v = llList2Vector(result, 1);
        integer vz = llCeil(v.z);
        string sz = "   " + (string) vz;
        sz = llGetSubString(sz, -3, -1) + " ";
        // return (string)x+":"+sz;
        return sz;
    }
}

string scan_row(integer y) {
    string ys = llGetSubString("000" + (string) y, -3, -1);
    string row = ys + ": ";
    integer x;
    for (x = 1; x <= 255; x+=2) {
        row += scan(x, y, 255);
    }
    return row + "//";
}

default {
    on_rez(integer start_param) {
        llResetScript();
    }

    state_entry() {
        run_tests();
        llListen(0, "", llGetOwner(), "");
        llSetText("Landcaster", <0,1,0>, 1);
        Query = llRequestURL();
    }

    http_request(key id, string method, string body) {
        if ( id == Query ) {
          if ( method == URL_REQUEST_GRANTED ) {
            URL = body;
            URL += "/";
            llSay(0, "URL: " + URL);
          } else if ( method == URL_REQUEST_DENIED ) {
            llOwnerSay("denied");
          }
        } else if ( method == "GET" ) {
            string args = llGetHTTPHeader(id, "x-query-string");
            integer row = (integer)args;
            if (row != 0) {
                string response = scan_row(row);
                llHTTPResponse(id, 200, response);
                llSay(0, response);
            } else {
                llHTTPResponse(id, 200, "bad row " + args);
                llSay(0, "bad row " + args);
            }
        }
    }


    listen(integer channel, string name, key id, string message) {
        if (message == "test" ) {
            run_tests();
        } else if (llSubStringIndex(message, "scan") == 0 ) {
            integer y = (integer) llGetSubString(message, 5, -1);
            llOwnerSay("Scanning " + (string) y);
            llOwnerSay(scan_row(y));
        }
    }

    touch_start(integer num_detected) {
        llSay(0, URL);
        string row = scan_row(3);
        // llOwnerSay( (string) llStringLength(row));
        // llOwnerSay(row);
    }
}