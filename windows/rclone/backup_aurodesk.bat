if "%1"=="hide" goto CmdBegin
start mshta vbscript:createobject("wscript.shell").run("""%~0"" hide",0)(window.close)&&exit
:CmdBegin
rclone sync "D:\Data\Aurorataro" onedrive:Public/Personal/Aurorataro --transfers 8
rclone sync "D:\Data\FFXIV\FFXIV screenshot" onedrive:Public/Personal/Sync/FinalFantansy/screenshots --transfers 8
rclone sync "E:\Game\FF14\   ջ   XIV\game\My Games\FINAL FANTASY XIV - A Realm Reborn" onedrive:Public/Personal/Sync/FinalFantansy/config --filter-from "filter-list.txt" --transfers 8