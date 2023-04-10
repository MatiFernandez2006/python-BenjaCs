class Mathdojo:
      def __init__(self):
            self.resultado = 0

      def suma(self, *args):
            for arg in args:
                  self.resultado += arg
            return self
      
      def resta(self, *args):
            for arg in args:
                  self.resultado += arg
            return self
      
md = Mathdojo()

md.sumar(31, 23, 20)
print(md.resultado)

md.sumar(1).sumar(2,3).sumar(44, 56, 68)
print(md.resultado)

md.restar(23, 12, 23)
print(md.resultado)

md.restar(6).restar(3, 2).restar(3, 12, 16)
print(md.resultado)