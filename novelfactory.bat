@echo off
REM ============================================================================
REM  NOVEL FACTORY - command launcher (Windows)
REM
REM  Usage:  novelfactory.bat <command> <project> [options...]
REM
REM  Create LLM script :  novelfactory.bat new my_episode --title "The Silent Contract"
REM  Ingest script     :  novelfactory.bat ingest my_episode script_part1.json script_part2.json
REM  Demo episode      :  novelfactory.bat demo my_episode
REM  Validate master   :  novelfactory.bat validate my_episode
REM  ChatGPT queue     :  novelfactory.bat frames my_episode
REM  Omni queue        :  novelfactory.bat omni my_episode
REM  Muse AI queue     :  novelfactory.bat muse my_episode
REM  Flow/Veo queue    :  novelfactory.bat flow my_episode
REM  Master prompts    :  novelfactory.bat prompts my_episode
REM  Workflow prompts  :  novelfactory.bat export-master-prompts my_episode
REM  Status            :  novelfactory.bat status my_episode
REM  Clip assistant    :  novelfactory.bat assisted my_episode
REM  Watch downloads   :  novelfactory.bat watch my_episode --once
REM  Import frames     :  novelfactory.bat import-frames my_episode --frames-src "C:\path\frames"
REM  Dashboard         :  novelfactory.bat dashboard my_episode --serve --open
REM  Assemble          :  novelfactory.bat assemble my_episode
REM  Preflight only    :  novelfactory.bat check my_episode
REM  Export queue      :  novelfactory.bat publish my_episode --apply
REM  Offline tests     :  novelfactory.bat test
REM ============================================================================
setlocal enabledelayedexpansion
REM IMPORTANT: capture the .bat folder BEFORE shifting arguments.
REM (shift also shifts %0, so %~dp0 would no longer be reliable.)
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
if /i "%CMD%"=="muse-pack" ( set "SCRIPT=generators\05_export_muse_method_pack.py" & goto :RUN )
if /i "%CMD%"=="prepare"  goto :PREPARE
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
echo  [!] Unknown command: %CMD%
goto :HELP

:PREPARE
echo.
python "%NFDIR%nf_core.py" prepare !REST!
if errorlevel 1 (
  echo.
  echo  [X] prepare finished with errors ^(code %errorlevel%^).
)
goto :DONE

:INGEST
REM  ingest <slug> <json...>  ->  --ingest must come BEFORE the JSON list
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
  echo  [!] Usage: novelfactory.bat ingest ^<slug^> ^<json...^>
  goto :DONE
)
python "%NFDIR%generators\01_story_to_master_json.py" "!SLUG!" --ingest !FILES!
if errorlevel 1 ( echo. & echo  [X] Ingest finished with errors. )
goto :DONE

:RUN
echo.
python "%NFDIR%%SCRIPT%" !REST! %MODE%
if errorlevel 1 (
  echo.
  echo  [X] The command finished with errors ^(code %errorlevel%^).
)
goto :DONE

:HELP
echo.
echo  NOVEL FACTORY - available commands:
echo.
echo    new ^<slug^> [--title "..."]        Generate brief + prompt-pack for the LLM
echo    ingest ^<slug^> ^<json...^>           Ingest the LLM's JSON script
echo    demo ^<slug^>                         Calibration demo episode (no LLM)
echo    validate ^<slug^>                     Validate master_episode.json
echo    frames ^<slug^>                       Export the image queue (ChatGPT)
echo    omni ^<slug^>                         Export the video queue (Omni)
echo    muse ^<slug^>                         Export the video queue (Muse AI)
echo    flow ^<slug^>                         Export the video queue (Google Flow / Veo)
echo    prompts ^<slug^>                      Export the 4 filled master prompts
echo    export-master-prompts ^<slug^>        Generate workflow 000-003 + Muse AI batches (6 scenes)
echo    muse-pack ^<slug^>                    Single package: 11 images + 10 Muse AI batches
echo    prepare ^<slug^>                       Regenerate workflow 00 + 04 + Muse package 05
echo    status ^<slug^>                       Clip/frame progress table
echo    queue ^<slug^>                        Next pending prompt in the console
echo    assisted ^<slug^>                     Clipboard assistant for Omni
echo    watch ^<slug^> [--once]               Watch Downloads and file clips
echo    import-frames ^<slug^> --frames-src DIR  Import existing frames into raw_frames
echo    dashboard ^<slug^> [--serve] [--open]  Dashboard to copy prompts and track scenes
echo    check ^<slug^>                        Assembly preflight (no render)
echo    assemble ^<slug^>                     Assemble 16:9 master + 9:16 teasers
echo    publish ^<slug^> [--apply]            Export teasers to the publisher queue
echo    test                                 Run the offline tests
echo.
echo  Full example:
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
