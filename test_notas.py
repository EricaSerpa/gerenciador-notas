# --- test_notas.py ---
"""Ambiente de Testes Automatizados do Sistema de Notas.

Script paralelo focado em validar a robustez matemática do sistema, cobrindo
cenários normais de uso e casos extremos limitadores (Edge Cases).
"""

import unittest

# Importação direta das rotinas funcionais para isolamento de testes
from gerenciador_notas import calcular_media, verificar_aprovacao


class TestSistemaNotas(unittest.TestCase):
    """Bateria de ensaios estruturada usando o framework nativo unittest do

    Python.
    """

    # -------------------------------------------------------------------------
    # 1. Validações de Cenários Comuns (Happy Paths)
    # -------------------------------------------------------------------------

    def test_calcular_media_comum(self):
        """Testa o cálculo da média com valores flutuantes tradicionais."""
        notas_aluno = [8.0, 7.0, 9.0]
        self.assertAlmostEqual(calcular_media(notas_aluno), 8.0)

    def test_verificar_aprovacao_comum(self):
        """Testa o retorno 'Aprovado' para notas na linha de corte e acima."""
        self.assertEqual(verificar_aprovacao(7.5), "Aprovado")
        self.assertEqual(verificar_aprovacao(7.0), "Aprovado")

    def test_verificar_reprovacao_comum(self):
        """Testa o retorno 'Reprovado' para notas abaixo do critério mínimo."""
        self.assertEqual(verificar_aprovacao(6.9), "Reprovado")
        self.assertEqual(verificar_aprovacao(4.5), "Reprovado")

    # -------------------------------------------------------------------------
    # 2. Validações de Casos Extremos (Edge Cases)
    # -------------------------------------------------------------------------

    def test_calcular_media_lista_vazia(self):
        """Testa a resiliência do sistema com uma lista de notas totalmente

        vazia, garantindo que não ocorra interrupção por ZeroDivisionError.
        """
        lista_vazia = []
        self.assertEqual(calcular_media(lista_vazia), 0.0)

    def test_verificar_aprovacao_corte_zero(self):
        """Testa a estabilidade do sistema ao configurar parâmetros limites de

        negócio, como uma média mínima de aprovação igual a 0.0.
        """
        self.assertEqual(verificar_aprovacao(5.0, media_minima=0.0), "Aprovado")
        self.assertEqual(verificar_aprovacao(0.0, media_minima=0.0), "Aprovado")


if __name__ == "__main__":
    unittest.main()
