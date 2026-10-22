# XMB Menu True Ratio for ES-DE

A fork of [XMB Menu for ES-DE](https://github.com/anthonycaccese/xmb-menu-es-de) by Ant and InitialDin. Title screen and fanart slots get their console's true screen ratio (PSP 16:9, GameCube 4:3, Game Boy 10:9, …), the game video plays in that ratio in every variant, and new variants keep the XMB background behind the carousel. See [True Ratio variants](#true-ratio-variants) below; everything else works as in the original theme.

From the original README:

> This is a translation of the PSP XMB menu for ES-DE. The xml was originally built by InitialDin and I've done a refactor to clean up image assets, add color scheme support, customizations and additional aspect ratios. This repository will maintain our shared work so that it can be used with ES-DE's theme downloader.

## **Preview**

![Preview](https://github.com/user-attachments/assets/77926f1b-1f0c-4a21-873a-b7191ce26c31)

## **Configuration Options**

- The theme has a simple set of options that can be changed directly from the UI Settings menu of ES-DE 
- `Theme Variant` - Sets the layout used for the gamelist view when media & metadata are scraped for your games.  There are 11 variants to choose from:
   - `Boxart` - A simple carousel that displays game cover artwork
   - `Marquee` - A simple carousel that displays game marquee artwork
   - `Title Screen` - A simple carousel that displays game title screens
   - `Physical Media` - A simple carousel that displays game physical media
   - `Boxart + Marquee`, `Title Screen + Marquee`, `Physical Media + Marquee` - The same carousels with the game marquee in the bottom right corner
   - `Fanart (XMB)`, `Fanart + Marquee (XMB)`, `Title Screen (XMB)`, `Title Screen + Marquee (XMB)` - See [True Ratio variants](#true-ratio-variants)
- `Theme Color Scheme` - Sets the color scheme, system artwork and system logo used on all views.  This can be customized by following the instructions in the [Customizations](#customizations) section below.
- `Theme Font Size` - Sets the font size to use. I've included font sizes built to scale well from small handheld screens all the way up through larger tv screens.
- `Theme Aspect Ratio` - Sets the aspect ratio that the theme will render at. This should happen automatically but if needed, this can be changed manually to match the aspect ratio of your screen.  16:9, 16:10, 4:3, 3:2, 8:7, 20:9 and 1:1 are supported

### **Built-in Color Schemes**

<table>
   <tr>
      <td><img src="https://github.com/user-attachments/assets/77926f1b-1f0c-4a21-873a-b7191ce26c31"/></td>
      <td><img src="https://github.com/user-attachments/assets/ad8b41a9-a561-41c9-b8eb-2751417640b8"/></td>
      <td><img src="https://github.com/user-attachments/assets/f66de94a-09de-43e9-ae5e-e643b5f1ea60"/></td>
   </tr>
   <tr>
      <td><img src="https://github.com/user-attachments/assets/bae1eb32-3ceb-4bd8-a5a9-d7cc85e5fe57"/></td>
      <td><img src="https://github.com/user-attachments/assets/119dcf12-6b6f-448f-a173-398a7e8d7121"/></td>
      <td><img src="https://github.com/user-attachments/assets/c48b276c-4e3a-499b-af8a-4f3182166f9f"/></td>
   </tr>
   <tr>
      <td><img src="https://github.com/user-attachments/assets/7fa3187b-4330-4cce-bb3b-a1d390358037"/></td>
      <td><img src="https://github.com/user-attachments/assets/ddca37a8-1538-45f7-9c60-85f16b7edbcb"/></td>
      <td><img src="https://github.com/user-attachments/assets/6c906b31-1461-4a8d-b97b-b506723f6dca"/></td>
   </tr>
</table>

## **True Ratio variants**

- **All variants:** the game video plays in the console's screen ratio, as big as the selected slot, and games without the image get an empty glass box instead of their name (the name is already shown next to the slot)
- **`Boxart` and `Physical Media`** (each also with a marquee): every slot has the shape of the console's cover or cartridge (`systemCoverSize` / `systemCartSize`), so covers fit exactly and the glass box has the same shape
- **`Title Screen`, `Title Screen (XMB)` and `Fanart (XMB)`** (each also with a marquee): every slot has the screen ratio of its console, and the image is cropped to fill it (no stretching, no letterboxing). The video covers the selected slot exactly.
- **The `(XMB)` variants** also:
   - keep the XMB background visible; the game art is shown in the carousel instead of behind it
   - show the marquee at full brightness (the other variants dim it, because the fanart background is behind it)

Marquee slots keep their original shape, because logos have no fixed shape.

### **Screen ratio per console**

| Ratio | Consoles |
|---|---|
| `16-9` | PSP, PS Vita, Switch, Wii U, PS3, PS4, Xbox 360, Xbox One, Virtual Boy, Playdate, PC/Steam/Windows, Android |
| `3-2` | Game Boy Advance, Lynx, WonderSwan (Color), Pokémon Mini |
| `10-9` | Game Boy, Game Boy Color, Game Gear, Mega Duck |
| `1-1` | Neo Geo Pocket (Color), Supervision, Gamate |
| `2-3` | Nintendo DS (both screens stacked) |
| `screen` | All Games, Favorites, Last Played and collections (same shape as your screen) |
| `4-3` | Every other system |

To change a console, edit `<systemScreenRatio>` in its file in `_inc/systems/_metadata-global/` (for example `gc.xml`). A system without its own value uses `_default.xml`. The slot and video sizes for every screen and console ratio are in `_inc/screen-ratio/<screen ratio>/<console ratio>.xml`. Cover and cartridge slots work the same way with `_inc/box-ratio/<screen ratio>/<systemCoverSize or systemCartSize>.xml`. Slots never get bigger than the original boxart slot, so tall ratios get narrower instead of taller.

The glass box colour is `textBackgroundColor` / `textSelectedBackgroundColor` in the `gamelist-carousel` of `theme.xml` (default `FFFFFF22`; the last two digits are the opacity).

## **Customizations**

### **Creating your own color scheme**

A custom color scheme lets you to modify any of the colors and backgrounds used in the theme while also allowing you to continue to get updates from the theme downloader.

#### Instructions:

1) In the resources folder you will find a template file called [custom.xml](https://github.com/josuacodes/xmb-menu-true-ratio-es-de/blob/main/resources/custom.xml)

2) Place a copy of that file into the `theme-customizations` folder. The folder structure should look like this when you are done:
   ```
   /ES-DE/themes/xmb-menu-true-ratio-es-de/theme-customizations/custom.xml
   ```

3) Edit the properites in `custom.xml` to create your custom color scheme.  All properties are optional so you only need to include the properties you actually change.  Any others can be removed and will fallback automatically to defaults.
   - Here is a definition of each property:
      - `iconColor` - Sets the color of icons used across the theme
      - `textColor` - Sets the color of text used across the theme
      - `lineColor` - Sets the color of the line that is shown in the middle of the screen
      - `backgroundImagePath` - Sets the path to the image you would like to display as your background 
      - `backgroundVideoPath` - If you have `showBackgroundVideo` set to true then this sets the path to the video you would like to display as your background
      - `backgroundImageTile` - If you would like to set a solid color background instead of an image then set this to `true` and set `backgroundImagePath` to `${spacerImage`
      - `backgroundColor` & `backgroundColorEnd` - sets the colors to use for the background image and video.  If you would like a gradient then set a different hex value for each and if you would like one solid color then set the same hex value for each.
      - `backgroundGradientType` - if you set a gradient then this sets the direction the gradient will display as.  Options are: `horizontal`, `vertical`
      - `backgroundGameArtType` - If you have `showBackgroundGameArtSystemView` or `showBackgroundGameArtGamelistView` set to true then this property sets the type of gameart to display. Options are: `fanart`, `screenshot`
      - `backgroundGameArtSelector` - If you have `showBackgroundGameArtSystemView` then this property sets the query to use for pulling in game art.  Options are: `lastplayed`, `random`
      - `showBackgroundGameArtSystemView` - Sets if you would like to display video backgrounds.  If you set this then make sure to set a value for `backgroundVideoPath`
      - `showBackgroundGameArtSystemView` - Sets if you would like to display game art backgrounds as you scroll through systems on the system view.
      - `showBackgroundGameArtGamelistView` - Sets if you would like to display game art backgrounds as you scroll through games on the gamelist view
    
4) Set the `Theme Color Scheme` in ES-DE's UI Settings menu to `Custom` and you should see your custom color scheme display.  If you see an error check that the paths discussed above are correct and then check that the values you added for each property are correct and well formatted.

### **Example**

Here is a preview of what is possible through customizations along with the XML that was written for it.  Note: the custom.xml below only contains properties that were changed. When creating a custom.xml you only need to provide the properties you actually change.

<table>
   <tr>
      <td><img src="https://github.com/user-attachments/assets/6cdc5f94-d185-490b-a414-16e27c23ba79" /></td>
      <td><img src="https://github.com/user-attachments/assets/572e2325-f851-49d4-ae61-2119be7699a3" /></td>
   </tr>
</table>

```xml
<theme>
   <colorScheme name="custom">
      <variables>
         <!-- Color Settings -->
         <iconColor>111111</iconColor>
         <textColor>111111</textColor>
         <lineColor>11111133</lineColor>
         <!-- System Image Settings -->
         <systemCarouselImagePath>./theme-customizations/20th-anniversary/controllers</systemCarouselImagePath>
         <systemCarouselImageColor>ffffff</systemCarouselImageColor>
         <systemContentImageColor>777777</systemContentImageColor>
         <!-- Static Background Settings -->
         <backgroundImagePath>./theme-customizations/20th-anniversary/background.png</backgroundImagePath>
         <backgroundColor>ffffff</backgroundColor>
         <backgroundColorEnd>ffffff</backgroundColorEnd>
         <!-- Background Display Settings -->
         <showBackgroundVideo>false</showBackgroundVideo>
         <showBackgroundGameArtSystemView>false</showBackgroundGameArtSystemView>
         <showBackgroundGameArtGamelistView>false</showBackgroundGameArtGamelistView>
      </variables>
   </colorScheme>
</theme>
```

## **Credits**

- Inspired by the design of the Cross Media bar by Sony for the PSP &amp; PS3
- The orignal XML for this theme was created by InitialDin
- [XMB Menu for ES-DE](https://github.com/anthonycaccese/xmb-menu-es-de), which this fork is based on, is maintained by Ant ([anthonycaccese](https://github.com/anthonycaccese))
- The True Ratio variants were added in this fork by [josuacodes](https://github.com/josuacodes)
- System Controller Icons were sourced from [RobZombie9043](https://github.com/RobZombie9043) work in https://github.com/RobZombie9043/xmb-es-de
- System Physical Media Icons were sourced from RetroArch's XMB monochrome theme in https://github.com/libretro/retroarch-assets/tree/master/xmb/monochrome

## **License**

Creative Commons CC-BY-NC-SA - https://creativecommons.org/licenses/by-nc-sa/2.0/
You are free to share and adapt this theme as long as you provide attribution back to me (and the above credits) as well share any updates you make under the same licence terms.
