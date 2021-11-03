# SFU Phd Thesis

## Included files from ATLAS repo
  
The ATLAS document class (`atlasdoc.cls`) and style files can be found in 
the latex directory. The following main style files exist:

- `atlasbiblatex.sty`:  Reference style adjustments for `biblatex`
- `atlascover.sty`:     Make a cover (CONF note, CERN preprint, ATLAS draft)
- `atlascontribute.sty`: List of contributors (and authors) for a document
- `atlaspackage.sty`:   Standard packages used in ATLAS documents
- `atlasphysics.sty`:   Useful definitions. This file simply inputs others.

Options can be used to specify which should be included.

Documentation can be found via the ATLAS TWiki page:
<https://twiki.cern.ch/twiki/bin/view/AtlasProtected/PubComLaTeX>

The following documents are available in subdirectories of the `doc` and `template` directories or as artifacts in the GitLab repository:
* [Users guide to the ATLAS LaTeX package](https://gitlab.cern.ch/atlas-physics-office/atlaslatex/-/jobs/artifacts/master/file/doc/atlas_latex/atlas_latex.pdf?job=build_user) - also in `doc/atlas_latex`
* [Guide to references and BibTeX in ATLAS documents](https://gitlab.cern.ch/atlas-physics-office/atlaslatex/-/jobs/artifacts/master/file/doc/atlas_bibtex/atlas_bibtex.pdf?job=build_bibtex) - also in `doc/atlas_bibtex`
* [ATLAS physics symbols](https://gitlab.cern.ch/atlas-physics-office/atlaslatex/-/jobs/artifacts/master/file/doc/atlas_physics/atlas_physics.pdf?job=build_physics) - also in `doc/atlas_physics`
* [ATLAS physics symbols with hepparticle](https://gitlab.cern.ch/atlas-physics-office/atlaslatex/-/jobs/artifacts/master/file/doc/atlas_physics/atlas_hepphysics.pdf?job=build_physics) - also in `doc/atlas_physics`
* [Guide to formatting tables for ATLAS documents](https://gitlab.cern.ch/atlas-physics-office/atlaslatex/-/jobs/artifacts/master/file/doc/atlas_tables/atlas_tables.pdf?job=build_tables) - also in `doc/atlas_tables`



## How to use

Simply run `make` to compile.

Four other make targets are:

- `make clean`: cleans up intermediate files
- `make cleanpdf`: remove output pdf file
- `make cleanall`: also cleans up output pdf file
- `make verson`: check your TeX Live version
