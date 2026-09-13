

Vencord Comfy theme by [Nyria](https://github.com/Comfy-Themes/Discord.git) with a few fixes and snippets from the official Comfy Discord server.

Used fork by [Metro420yt](https://github.com/Metro420yt/ClassUpdate) from [Saltssaumure](https://github.com/Saltssaumure/ClassUpdate) inspired by [SyndiShanX](https://github.com/SyndiShanX/Update-Classes) for a github action.

If you find any inconsistencies or unfixed bugs, please report them by opening an issue.
Moved most of the fixes I had in my comfy.css to fixes.css. After being satisfied with my fixes, I will append the fixes to main.css 

You could also reach out to me via. Discord: #abdist

# Usage
## 1. Online themes field in Vencord/Vesktop:
Add the following URL to the Online Themes section in the Vencord/Vesktop tab inside your user settings 

`[Settings > Vencord Settings > Themes > Online Themes]:`  
[https://raw.githubusercontent.com/Abdisto/comfy/main/comfy/comfy.css](https://raw.githubusercontent.com/Abdisto/comfy/main/comfy/comfy.css)

**OR** Add your own list of components you want, e.g.
```
https://raw.githubusercontent.com/Abdisto/comfy/main/comfy/main.css
https://raw.githubusercontent.com/Abdisto/comfy/main/comfy/user-waves-nyan.css
https://comfy-themes.github.io/Discord/betterdiscord/no-scrollbar.css
https://comfy-themes.github.io/Discord/betterdiscord/better-spotify.css
https://raw.githubusercontent.com/Abdisto/comfy/main/comfy/banner.css
https://raw.githubusercontent.com/Abdisto/comfy/main/comfy/ownerCrown.css
https://raw.githubusercontent.com/Abdisto/comfy/main/comfy/fixes.css
https://raw.githubusercontent.com/Abdisto/comfy/refs/heads/catppuccin-mocha-lavender-colors/comfy/colors.css
```
**OR** add your own colors.css similar to my branch with Catppuccin colors, e.g.
```
https://raw.githubusercontent.com/Abdisto/comfy/main/comfy/colors.css
```
## 2. QuickCSS field in Vencord/Vesktop:
Add the following to the QuickCSS section in the Vencord/Vesktop tab inside your user settings 

`[Settings > Vencord Settings > Vencord > Edit QuickCSS]:`  
`@import "https://raw.githubusercontent.com/Abdisto/comfy/main/comfy/comfy.css";`

Similar to **1.** you can add the components you want, e.g.
```
@import "https://raw.githubusercontent.com/Abdisto/comfy/main/comfy/main.css";
@import "https://raw.githubusercontent.com/Abdisto/comfy/main/comfy/user-waves-nyan.css";
@import "https://comfy-themes.github.io/Discord/betterdiscord/no-scrollbar.css";
@import "https://comfy-themes.github.io/Discord/betterdiscord/better-spotify.css";
@import "https://raw.githubusercontent.com/Abdisto/comfy/main/comfy/banner.css";
@import "https://raw.githubusercontent.com/Abdisto/comfy/main/comfy/ownerCrown.css";
@import "https://raw.githubusercontent.com/Abdisto/comfy/main/comfy/fixes.css";
/* @import "https://raw.githubusercontent.com/Abdisto/comfy/main/comfy/colors.css"; */
@import "https://raw.githubusercontent.com/Abdisto/comfy/refs/heads/catppuccin-mocha-lavender-colors/comfy/colors.css";
```
You can also remove colors.css and add your own colors by adding the contents of colors.css and changing the values.
