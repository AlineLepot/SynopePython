# coding: utf8
from six.moves import range

# """
# Renvoie une liste de points espacés de manière régulière
# pour un intervalle donné.
#
# Paramètres
# ==========
#
# begin : borne inférieure de l'intervalle
#
# end : borne supérieure de l'intervalle
#
# n : nombre de points
#
# Sortie
# ======
#
# Renvoie la liste des points de discrétisation.
#
# """
def linspace(begin, end, n):
  h = (end - begin)/(n-1)
  return [begin + i*h for i in range(n)]
