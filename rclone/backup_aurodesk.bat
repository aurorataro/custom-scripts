rclone sync "E:\Data\Aurorataro" onedrive:Public/Personal/Aurorataro --transfers 8 --progress
rclone sync "E:\Data\FFXIV\FFXIV screenshot" onedrive:Public/Personal/Sync/FinalFantansy/screenshots --transfers 8 --progress
rclone sync "D:\Games\FinalFantasy14\FF14\◊Ó÷’ª√œÎXIV\game\My Games\FINAL FANTASY XIV - A Realm Reborn" onedrive:Public/Personal/Sync/FinalFantansy/config --filter-from "filter-list.txt" --transfers 8 --progress
rclone copy "E:\WindowsUserFile\Video" onedrive:Public/Windows/Video --transfers 8 --progress
rclone sync "E:\WindowsUserFile\picture" onedrive:Public/Windows/Picture --transfers 8 --progress
rclone sync "E:\WindowsUserFile\documents" onedrive:Public/Windows/Document --transfers 8 --progress
rclone sync "E:\WindowsUserFile\Desktop" onedrive:Public/Windows/Desktop --transfers 8 --progress