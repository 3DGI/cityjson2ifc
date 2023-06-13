import pytest

from cityjson2ifc_cli.convert import cityjson2ifc


@pytest.mark.parametrize("input_model", ["input_model_5907", "input_model_68dn2"])
def test_lod_select(request, input_model, tmp_dir):
    """Can we extract a specific LoD?"""
    cm = request.getfixturevalue(input_model)
    outfile = tmp_dir / "outfile.ifc"
    cityjson2ifc(cm=cm, file_destination=str(outfile),
                 lod_select="1.2")


def test_lod_split(input_model_5907, tmp_dir):
    """Can we export one IFC per LoD?"""
    cm = input_model_5907
    outfile = tmp_dir / "outfile.ifc"
    cityjson2ifc(cm=cm, file_destination=str(outfile), lod_split=True)


def test_semantic_surfaces_building(input_model_5907, tmp_dir):
    """Can convert the Building's semantic surfaces?"""
    cm = input_model_5907
    outfile = tmp_dir / "outfile.ifc"
    cityjson2ifc(cm=cm, file_destination=str(outfile), lod_select="2.2")


@pytest.mark.parametrize("input_model,name_entity", [
    ("input_model_5907", "identificatie"),
    ("input_model_68dn2", "3df_id")]
)
def test_names(request, input_model, name_entity, tmp_dir):
    """Can we assign the various names?"""
    cm = request.getfixturevalue(input_model)
    outfile = tmp_dir / "outfile.ifc"
    cityjson2ifc(cm=cm, file_destination=str(outfile),
                 name_entity=name_entity, name_site="site-1234",
                 name_project="project-1234", name_person_given="me",
                 name_person_family="me me")
