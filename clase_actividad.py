class actividad:
  def __init__(self, nombre, tipo, presupuesto, gasto_real):
    self.nombre      = nombre
    self.tipo        = tipo
    self.presupuesto = presupuesto
    self.gasto_real  = gasto_real

  def esta_en_presupuesto(self):
    if self.gasto_real <= self.presupuesto:
      return True
    else:
      return False

  def mostrar_info(self):
    return {
        "nombre": self.nombre,
        "tipo": self.tipo,
        "presupuesto": self.presupuesto,
        "gasto_real": self.gasto_real,
        "esta_en_presupuesto": self.esta_en_presupuesto()
    }
