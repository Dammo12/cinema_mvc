from model.c_model import Model

m = Model()

t = m.create_movie('Rojo Amanecer', '02:30:45', '2020-05-22', '2020-06-22')
print(t)

t = m.read_movie(2)
print(t)