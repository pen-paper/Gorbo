class Model(object):
    def __init__(self, model):
        vertices = []
        textures = []
        normals = []
        combined_vertices = []
        faces = []
        for line in model:
            if line.startswith(b"#"):
                pass
            elif line.startswith(b"o"):
                pass
            elif line.startswith(b"s"):
                pass
            elif line.startswith(b"v "):
                x, y, z = line.split()[1:]
                vertices.append((float(x), float(y), float(z)))
            elif line.startswith(b"vt "):
                u, v = line.split()[1:]
                textures.append((float(u), float(v)))
            elif line.startswith(b"vn "):
                x, y, z = line.split()[1:]
                normals.append((float(x), float(y), float(z)))
            elif line.startswith(b"f "):
                a, b, c = line.split()[1:]
                for corner in (a, b, c):
                    v, t, n = corner.split(b"/")
                    if (v, t, n) in combined_vertices:
                        faces.append(combined_vertices.index((v, t, n)))
                    else:
                        faces.append(len(combined_vertices))
                        combined_vertices.append((v, t, n))
            else:
                raise ValueError("What is this line?\n{}".format(line))
        self.vertices = []
        self.tex_coords = []
        self.normals = []
        self.indices = []
        self.num_verts = len(combined_vertices)
        for v, t, n in combined_vertices:
            self.vertices.extend(vertices[int(v)-1])
            self.tex_coords.extend(textures[int(t)-1])
            self.normals.extend(normals[int(n)-1])
        for i in faces:
            self.indices.append(i)
