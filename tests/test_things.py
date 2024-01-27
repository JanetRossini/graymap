

class TestThings:
    def test_hookup(self):
        assert 2 + 2 == 4

    def test_first_read(self):
        name = "/Users/ron/Dropbox/ph-heights.txt"
        with open(name) as f:
            line = f.readline()
        assert len(line) == 520

    def test_trim_line(self):
        name = "/Users/ron/Dropbox/ph-heights.txt"
        with open(name) as f:
            line = f.readline()
        trim = line[4:-3]
        print(trim)
        assert len(trim) == 513
        subs = trim.split()
        assert len(subs) == 128
        ints = [int(s) for s in subs]
        assert ints[0] == 26
        assert ints[127] == 40

    def test_get_all_ints(self):
        name = "/Users/ron/Dropbox/ph-heights.txt"
        rows = []
        with open(name) as f:
            for line in f:
                trim = line[4:-3]
                subs = trim.split()
                ints = [int(s) for s in subs]
                rows.append(ints)
        assert len(rows) == 128

    def test_simpler(self):
        name = "/Users/ron/Dropbox/ph-heights.txt"
        rows = []
        with open(name) as f:
            for line in f:
                ints = line_to_ints(line)
                rows.append(ints)
        assert len(rows) == 128

    def test_file_to_rows(self):
        name = "/Users/ron/Dropbox/ph-heights.txt"
        rows = file_to_rows(name)
        assert len(rows) == 128

    def test_max_and_min(self):
        name = "/Users/ron/Dropbox/ph-heights.txt"
        rows = file_to_rows(name)
        maximum = 0
        minimum = 256
        for row in rows:
            maximum = max(maximum, max(row))
            minimum = min(minimum, min(row))
        assert maximum == 249
        assert minimum == 26

    def test_make_verts(self):
        rows = [[10, 11, 12, 13], [20, 21, 22, 23], [30, 31, 32, 33]]
        n_rows = len(rows)
        n_cols = len(rows[0])
        assert n_rows == 3
        assert n_cols == 4
        verts = []
        for y, row in enumerate(rows):
            yy = 2 * y + 1
            for x, z in enumerate(row):
                xx = 2 * x + 1
                verts.append((xx, yy, z))
        assert len(verts) == n_rows * n_cols
        assert verts[0] == (1, 1, 10)
        assert verts[5] == (3, 3, 21)
        assert verts[10] == (5, 5, 32)

    def test_face_vert_indices(self):
        expected = [(0, 1, 5, 4),
                    (1, 2, 6, 5),
                    (2, 3, 7, 6),
                    (4, 5, 9, 8),
                    (5, 6, 10, 9),
                    (6, 7, 11, 10),
                    (8, 9, 13, 12),
                    (9, 10, 14, 13),
                    (10, 11, 15, 14)]
        n_rows = 4
        n_cols = 4
        n_faces = (n_rows - 1) * (n_cols - 1)
        assert n_faces == 9
        faces = []
        for row in range(n_rows - 1):
            row_origin = row * n_cols
            for col in range(n_cols - 1):
                lower_left = row_origin + col
                lower_right = lower_left + 1
                upper_right = lower_right + n_cols
                upper_left = upper_right - 1
                face = (lower_left, lower_right, upper_right, upper_left)
                faces.append(face)
        assert faces == expected


def file_to_rows(name):
    with open(name) as f:
        rows = [line_to_ints(line) for line in f]
    return rows


def line_to_ints(line):
    subs = line.split()
    trim = subs[1:-1]
    ints = [int(t) for t in trim]
    return ints
