import pytest
from egg_smol.bindings import EggSmolError, EGraph
from egg_smol.bindings_py import Variant


class TestEGraph:
    def test_parse_and_run_program(self):
        program = "(check (= (+ 2 2) 4))"
        egraph = EGraph()

        assert egraph.parse_and_run_program(program) == ["Checked."]

    def test_parse_and_run_program_exception(self):
        program = "(check (= 5 4))"
        egraph = EGraph()

        with pytest.raises(
            EggSmolError,
            match='Check failed: Value { tag: "i64", bits: 5 } != Value { tag: "i64", bits: 4 }',
        ):
            egraph.parse_and_run_program(program)

    def test_datatype(self):
        egraph = EGraph()
        egraph.declare_sort("Math")
        egraph.declare_constructor(Variant("Num", ["i64"]), "Math")
        egraph.declare_constructor(Variant("Var", ["String"]), "Math")
        egraph.declare_constructor(Variant("Add", ["Math", "Math"]), "Math")
        egraph.declare_constructor(Variant("Mul", ["Math", "Math"]), "Math")
