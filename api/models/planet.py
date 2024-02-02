from tools import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    climate = db.Column(db.String(100), nullable=False)
    diameter = db.Column(db.String(100), nullable=False)
    gravity = db.Column(db.String(100), nullable=False)
    orbital_period = db.Column(db.String(100), nullable=False)
    population = db.Column(db.String(100), nullable=False)
    rotation_period = db.Column(db.String(100), nullable=False)
    surface_water = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(200), nullable=False, unique=True)

    def __repr__(self):
        return "<Planet %r>" % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "orbital_period": self.orbital_period,
            "population": self.population,
            "rotation_period": self.rotation_period,
            "surface_water": self.surface_water,
            "url": self.url,
        }
