@echo off
REM ============================================================================
REM  NOVEL FACTORY ??? lanzador de comandos (Windows)
REM
REM  Uso:  novelfactory.bat <comando> <proyecto> [opciones...]
REM
REM  Crear guion LLM :  novelfactory.bat new mi_episodio --title "The Silent Contract"
REM  Ingerir guion   :  novelfactory.bat ingest mi_episodio guion_parte1.json guion_parte2.json
REM  Episodio demo   :  novelfactory.bat demo mi_episodio
REM  Validar maestro :  novelfactory.bat validate mi_episodio
REM  Cola ChatGPT    :  novelfactory.bat frames mi_episodio
REM  Cola Omni       :  novelfactory.bat omni mi_episodio
REM  Cola Muse AI    :  novelfactory.bat muse mi_episodio
REM  Cola Flow/Veo   :  novelfactory.bat flow mi_episodio
REM  Prompts maestros:  novelfactory.bat prompts mi_episodio
REM  Workflow prompts: novelfactory.bat export-master-prompts mi_episodio
REM  Estado          :  novelfactory.bat status mi_episodio
REM  Asistente clips :  novelfactory.bat assisted mi_episodio
REM  Vigilar descargas: novelfactory.bat watch mi_episodio --once
REM  Importar frames :  novelfactory.bat import-frames mi_episodio --frames-src "C:\ruta\frames"
REM  Dashboard       :  novelfactory.bat dashboard mi_episodio --serve --open
REM  Ensamblar       :  novelfactory.bat assemble mi_episodio
REM  Solo preflight  :  novelfactory.bat check mi_episodio
REM  Exportar cola   :  novelfactory.bat publish mi_episodio --apply
REM  Tests offline   :  novelfactory.bat test
REM ============================================================================
setlocal enabledelayedexpansion
REM IMPORTANTE: capturar la carpeta del .bat ANTES de mover argumentos.
REM (shift tambi??n desplaza %0, as?? que %~dp0 dejar??a de ser fiable.)
set "NFDIR=%~dp0"
cd /d "%NFDIR%"

set "CMD=%~1"
if "%CMD%"=="" goto :HELP
if /i "%CMD%"=="ingest" goto :INGEST
shift

set "REST="
:COLLECT
if "%~1"=="" goto :DISPATCH
set "REST=!REST! "%~1""
shift
goto :COLLECT

:DISPATCH
set "MODE="
if /i "%CMD%"=="new"      ( set "SCRIPT=generators\01_story_to_master_json.py" & goto :RUN )
if /i "%CMD%"=="demo"     ( set "SCRIPT=generators\01_story_to_master_json.py" & set "MODE=--template" & goto :RUN )
if /i "%CMD%"=="validate" ( set "SCRIPT=generators\01_story_to_master_json.py" & set "MODE=--validate" & goto :RUN )
if /i "%CMD%"=="frames"   ( set "SCRIPT=generators\02_export_chatgpt_queue.py" & goto :RUN )
if /i "%CMD%"=="omni"     ( set "SCRIPT=generators\03_export_omni_queue.py" & goto :RUN )
if /i "%CMD%"=="muse"     ( set "SCRIPT=generators\03_export_omni_queue.py" & set "MODE=--platform muse" & goto :RUN )
if /i "%CMD%"=="flow"     ( set "SCRIPT=generators\03_export_omni_queue.py" & set "MODE=--platform flow" & goto :RUN )
if /i "%CMD%"=="prompts"  ( set "SCRIPT=generators\04_export_master_prompts.py" & goto :RUN )
if /i "%CMD%"=="export-master-prompts" ( set "SCRIPT=generators\00_export_master_workflow_prompts.py" & goto :RUN )
if /i "%CMD%"=="status"   ( set "SCRIPT=automation\omni_flow_runner.py" & set "MODE=status" & goto :RUN )
if /i "%CMD%"=="queue"    ( set "SCRIPT=automation\omni_flow_runner.py" & set "MODE=queue" & goto :RUN )
if /i "%CMD%"=="assisted" ( set "SCRIPT=automation\omni_flow_runner.py" & set "MODE=assisted" & goto :RUN )
if /i "%CMD%"=="watch"    ( set "SCRIPT=automation\omni_flow_runner.py" & set "MODE=watch" & goto :RUN )
if /i "%CMD%"=="import-frames" ( set "SCRIPT=automation\omni_flow_runner.py" & set "MODE=import-frames" & goto :RUN )
if /i "%CMD%"=="dashboard" ( set "SCRIPT=automation\dashboard.py" & goto :RUN )
if /i "%CMD%"=="check"    ( set "SCRIPT=post_production\04_assemble_novel_ffmpeg.py" & set "MODE=--check" & goto :RUN )
if /i "%CMD%"=="assemble" ( set "SCRIPT=post_production\04_assemble_novel_ffmpeg.py" & goto :RUN )
if /i "%CMD%"=="publish"  ( set "SCRIPT=post_production\05_export_to_publisher.py" & goto :RUN )
if /i "%CMD%"=="test"     ( python -m unittest discover -s tests -v & goto :DONE )
echo  [!] Comando desconocido: %CMD%
goto :HELP

:INGEST
REM  ingest <slug> <json...>  ->  --ingest debe ir ANTES de la lista de JSON
shift
set "SLUG=%~1"
shift
set "FILES="
:INGEST_COLLECT
if "%~1"=="" goto :INGEST_RUN
set "FILES=!FILES! "%~1""
shift
goto :INGEST_COLLECT
:INGEST_RUN
if "!SLUG!"=="" (
  echo  [!] Uso: novelfactory.bat ingest ^<slug^> ^<json...^>
  goto :DONE
)
python "%NFDIR%generators\01_story_to_master_json.py" "!SLUG!" --ingest !FILES!
if errorlevel 1 ( echo. & echo  [X] La ingesta termin?? con errores. )
goto :DONE

:RUN
echo.
python "%NFDIR%%SCRIPT%" !REST! %MODE%
if errorlevel 1 (
  echo.
  echo  [X] El comando termin?? con errores ^(c??digo %errorlevel%^).
)
goto :DONE

:HELP
echo.
echo  NOVEL FACTORY ??? comandos disponibles:
echo.
echo    new ^<slug^> [--title "..."]        Genera brief + prompt-pack para el LLM
echo    ingest ^<slug^> ^<json...^>           Ingesta el guion JSON del LLM
echo    demo ^<slug^>                         Episodio demo de calibraci??n (sin LLM)
echo    validate ^<slug^>                     Valida master_episode.json
echo    frames ^<slug^>                       Exporta la cola de im??genes (ChatGPT)
echo    omni ^<slug^>                         Exporta la cola de v??deo (Omni)
echo    muse ^<slug^>                         Exporta la cola de v??deo (Muse AI)
echo    flow ^<slug^>                         Exporta la cola de v??deo (Google Flow / Veo)
echo    prompts ^<slug^>                      Exporta los 4 prompts maestros rellenados
echo    export-master-prompts ^<slug^>        Genera workflow 000-003 + lotes Muse AI (6 escenas)
echo    status ^<slug^>                       Tabla de progreso de clips/frames
echo    queue ^<slug^>                        Siguiente prompt pendiente por consola
echo    assisted ^<slug^>                     Asistente de portapapeles para Omni
echo    watch ^<slug^> [--once]               Vigila Descargas y archiva clips
echo    import-frames ^<slug^> --frames-src DIR  Importa frames existentes a raw_frames
echo    dashboard ^<slug^> [--serve] [--open]  Dashboard para copiar prompts y trackear escenas
echo    check ^<slug^>                        Preflight del ensamblaje (sin render)
echo    assemble ^<slug^>                     Ensambla master 16:9 + teasers 9:16
echo    publish ^<slug^> [--apply]            Exporta teasers a la cola del publicador
echo    test                                 Ejecuta los tests offline
echo.
echo  Ejemplo completo:
echo    novelfactory.bat demo demo_contract
echo    novelfactory.bat frames demo_contract
echo    novelfactory.bat omni demo_contract
echo    novelfactory.bat muse demo_contract
echo    novelfactory.bat flow demo_contract
echo    novelfactory.bat prompts demo_contract
echo    novelfactory.bat export-master-prompts demo_contract
echo    novelfactory.bat assemble demo_contract
echo.

:DONE
endlocal
