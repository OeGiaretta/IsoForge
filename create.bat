@echo off
title Criador de Estrutura - IsoForge

echo ====================================
echo        Criando IsoForge
echo ====================================

:: Pasta raiz
mkdir IsoForge
cd IsoForge

:: Código principal
mkdir isoforge

:: Core
mkdir isoforge\core
mkdir isoforge\core\math
mkdir isoforge\core\fields
mkdir isoforge\core\mesh
mkdir isoforge\core\algorithms

:: Renderer
mkdir isoforge\renderer

:: UI
mkdir isoforge\ui
mkdir isoforge\ui\windows
mkdir isoforge\ui\widgets
mkdir isoforge\ui\panels

:: Exportadores
mkdir isoforge\exporters

:: Exemplos
mkdir examples

:: Testes
mkdir tests

:: Arquivos Python
type nul > main.py

:: Core - Math
type nul > isoforge\core\math\__init__.py
type nul > isoforge\core\math\parser.py
type nul > isoforge\core\math\expression.py
type nul > isoforge\core\math\evaluator.py

:: Core - Fields
type nul > isoforge\core\fields\__init__.py
type nul > isoforge\core\fields\scalar_field.py
type nul > isoforge\core\fields\voxel_grid.py
type nul > isoforge\core\fields\sampler.py

:: Core - Mesh
type nul > isoforge\core\mesh\__init__.py
type nul > isoforge\core\mesh\mesh.py
type nul > isoforge\core\mesh\vertex.py
type nul > isoforge\core\mesh\triangle.py
type nul > isoforge\core\mesh\normals.py

:: Core - Algorithms
type nul > isoforge\core\algorithms\__init__.py
type nul > isoforge\core\algorithms\marching_cubes.py
type nul > isoforge\core\algorithms\marching_tetrahedra.py
type nul > isoforge\core\algorithms\smoothing.py

:: Renderer
type nul > isoforge\renderer\__init__.py
type nul > isoforge\renderer\camera.py
type nul > isoforge\renderer\scene.py
type nul > isoforge\renderer\viewport.py

:: UI
type nul > isoforge\ui\__init__.py
type nul > isoforge\ui\windows\main_window.py
type nul > isoforge\ui\widgets\equation_input.py
type nul > isoforge\ui\panels\settings_panel.py
type nul > isoforge\ui\panels\viewport_panel.py

:: Exporters
type nul > isoforge\exporters\__init__.py
type nul > isoforge\exporters\obj_exporter.py
type nul > isoforge\exporters\stl_exporter.py
type nul > isoforge\exporters\ply_exporter.py

:: Examples
type nul > examples\sphere.py
type nul > examples\torus.py
type nul > examples\heart.py
type nul > examples\gyroid.py

:: Tests
type nul > tests\test_parser.py
type nul > tests\test_marching_cubes.py

:: Projeto
type nul > README.md
type nul > requirements.txt
type nul > .gitignore

echo.
echo ====================================
echo      Estrutura criada com sucesso
echo ====================================

pause