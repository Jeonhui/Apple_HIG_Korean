Touch Bar
=========

The Touch Bar is a Retina display and input device located above the keyboard on supported MacBook Pro models.![A sketch of a touch bar above a Mac keyboard, suggesting the extension of a physical keyboard with custom controls. The image is overlaid with rectangular and circular grid lines and is tinted purple to subtly reflect the purple in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/40d58512c119cb3672f3d9479860a1f5/inputs-touch-bar-intro@2x.png)

Dynamic controls in the Touch Bar let people interact with content on the main screen and offer quick access to system-level and app-specific functionality based on the current context. For example, when people type text in a document, the Touch Bar could include controls for adjusting the font style and size. Or when viewing a location on a map, the Touch Bar could offer quick, one-tap access to nearby points of interest.

The following guidelines can help you provide a Touch Bar experience that people appreciate. For developer guidance, see [`NSTouchBar`](/documentation/appkit/nstouchbar)
 and [Xcode Help](https://help.apple.com/xcode)
.

A Touch ID sensor to the right of the Touch Bar supports fingerprint authentication for logging into the computer and approving App Store and Apple Pay purchases. On devices that include the Touch Bar (2nd generation), a physical Esc (Escape) key appears to the left of the Touch Bar.

By default, the right side of the Touch Bar displays an expandable region called the *Control Strip* that includes controls for performing system-level tasks such as invoking Siri, adjusting the brightness of the main display, and changing the volume. You can place app-specific controls in the *app region* to the left of the Control Strip. In Touch Bar (1st generation), an Esc button or other system-provided button may appear to the left of the app region, depending on the context.

![Screenshot of a Touch Bar second generation with callouts that indicate (from left to right) the locations of the app region and the control strip.](https://docs-assets.developer.apple.com/published/ef2354061bb9df207d2328033cf5d239/tb-b-overview@2x.png)Touch Bar (2nd generation)![Screenshot of a Touch Bar first generation with callouts that indicate (from left to right) the locations of the system button, the app region, and the control strip.](https://docs-assets.developer.apple.com/published/2aa1f4bfc6bdec13fb531954c8d17c4b/tb-overview@2x.png)Touch Bar (1st generation)People can configure the Touch Bar to suit their needs. For example, people can remove items or hide the Control Strip completely, in which case only the controls in the app region and the system button remain. Alternatively, people can hide the app region to view an expanded Control Strip.

 [Play](#) 
You can support additional customization within the app region by letting people add and remove items.

**In general, let people customize your app’s Touch Bar experience.** Provide reasonable defaults for important and commonly used functions, but let people make adjustments to support their individual working styles.

**Provide alternative text labels for your Touch Bar controls.** By providing alternative text for your controls in the Touch Bar, VoiceOver can audibly describe the controls, making navigation easier for people with visual disabilities (for guidance, see [Accessibility](/design/human-interface-guidelines/accessibility)
). Also create labels for any customizable Touch Bar controls that you provide so VoiceOver can describe these controls on the customization screen.

[Gestures](/design/human-interface-guidelines/touch-bar#Gestures)
-----------------------------------------------------------------

People use a subset of the standard gestures to interact with the Touch Bar.

### [Tap](/design/human-interface-guidelines/touch-bar#Tap)

People tap to activate a control, like a button, or select an item, such as an emoji, a color, or a segment in a segmented control.

 [Play](#) 
### [Touch and hold](/design/human-interface-guidelines/touch-bar#Touch-and-hold)

A touch and hold gesture initiates a control’s secondary action. In Mail, for example, tapping the Flag button adds a flag to a message, but touching and holding the button reveals a modal view that lets people change the flag’s color.

 [Play](#) 
### [Horizontal swipe or pan](/design/human-interface-guidelines/touch-bar#Horizontal-swipe-or-pan)

People use a horizontal swipe or pan to drag an element, like a slider thumb, or navigate through content, such as a list of dates or a group of photos in a scrubber.

 [Play](#) 
### [Multi-Touch](/design/human-interface-guidelines/touch-bar#Multi-Touch)

Although the Touch Bar supports Multi-Touch gestures — like a pinch — such gestures can be cumbersome for people to perform. In general, it’s best to use Multi-Touch gestures sparingly.

 [Play](#) 
[Best practices](/design/human-interface-guidelines/touch-bar#Best-practices)
-----------------------------------------------------------------------------

Keep the following guidance in mind as you design your app’s Touch Bar interfaces.

**Make the Touch Bar relevant to the current context on the main screen.** Identify the different contexts within your app. Then, consider how you can expose varying levels of functionality based on how your app is used.

**Use the Touch Bar as an extension of the keyboard and trackpad, not as a display.** Although the Touch Bar is a screen, its primary function is to serve as an input device — not a secondary display. People may glance at the Touch Bar to locate or use a control, but their primary focus is the main screen. Avoid displaying alerts, messages, scrolling content, static content, or anything else that distracts people from the main screen.

**Strive to match the look of the physical keyboard.** When possible, aim to design Touch Bar controls that resemble the size and color of keys in the physical keyboard.

**Avoid making functionality available only in the Touch Bar.** Not all devices have a Touch Bar, and people can turn off app controls in the Touch Bar if they choose. Always give people ways to perform tasks using the keyboard or trackpad.

**In a full-screen context, consider displaying relevant controls in the Touch Bar.** In full-screen mode, apps often hide onscreen controls and reveal them only when people call for them by, for example, moving the pointer to the top of the screen. If you support full screen, you can use the Touch Bar to give people persistent access to important controls without distracting them from the full-screen experience.

**Prefer controls that produce immediate results.** Ideally, Touch Bar controls give people quick ways to perform actions that would otherwise require extra time spent clicking controls or choosing from menus. Minimize Touch Bar controls that present additional choices, such as popovers. For guidance, see [Controls and views](/design/human-interface-guidelines/touch-bar#Controls-and-views)
.

**Be responsive to Touch Bar interactions.** Even when your app is busy doing work or updating the main screen, respond instantly when people use a Touch Bar control.

**When possible, people need to be able to start and finish a task in the Touch Bar.** Avoid making people switch to the keyboard or trackpad to complete a task unless the task requires more complex interface controls than the Touch Bar provides.

**Avoid using the Touch Bar for tasks associated with well-known keyboard shortcuts.** People don’t need Touch Bar controls for tasks such as find, select all, deselect, copy, cut, paste, undo, redo, new, save, close, print, and quit. People also don’t need redundant controls for key-based navigation, such as page up and page down.

**Accurately reflect the state of a control that appears in both the Touch Bar and on the main screen.** For example, if a button is unavailable on the main screen, make sure it’s unavailable in the Touch Bar.

**When responding to user interactions, avoid showing the same UI in both the Touch Bar and the main screen.** For example, when people click the onscreen Emoji & Symbols button in a new message window in Mail, they expect the Character Viewer to open on the main screen, not in the Touch Bar. Unless people interact with the same control in both places, avoid distracting people by displaying redundant UI.

### [Animation](/design/human-interface-guidelines/touch-bar#Animation)

**Avoid animation.** The Touch Bar is an extension of the keyboard, and people don’t expect animation in their keyboard. In addition, excessive or gratuitous animation can distract people from their work.

### [Color](/design/human-interface-guidelines/touch-bar#Color)

**Prefer standard controls and system icons.** The standard controls and system icons already use colors that work well in the Touch Bar. For a list of available system icons, see [Interface icons](/design/human-interface-guidelines/touch-bar#Interface-icons)
.

![Screenshot of a Touch Bar that contains Maps controls, such as the current location button and the drive, walk, and transit buttons for directions. All Maps buttons have gray fill and white glyphs and titles. The drive button is selected, which means that its fill is lighter.](https://docs-assets.developer.apple.com/published/83f65d547facd2e309df2a488a72ef51/TB_visualDesign_colorOne@2x.png)

**Use color tastefully and minimally.** In general, make the Touch Bar similar in appearance to the physical keyboard. Monochromatic colors tend to work best. If you must use colors in your controls, do so tastefully and primarily in temporary states; avoid using colors that appear overwhelming or out of place.

**Use color to denote prominence.** Color can draw the eye to important controls. Reserve blue for default controls and red for destructive controls.

**If you use color, choose a limited palette that coordinates with your app.** Subtle use of color is one way to communicate your brand.

![Screenshot of a Touch Bar that contains Calculator controls. The arithmetic operation buttons have orange fill and white glyphs. All other Calculator buttons have gray fill and white glyphs.](https://docs-assets.developer.apple.com/published/86c6856903bd5f3a639e68ef749d1105/TB_visualDesign_colorTwo@2x.png)

**Provide wide color artwork.** The Touch Bar supports a P3 color space that can produce richer, more saturated colors than sRGB. Use the Display P3 color profile at 16 bits per pixel (per channel) and export your artwork in the PNG format. For guidance, see [Color management](/design/human-interface-guidelines/color#Color-management)
.

Tip

On a Mac that features a wide color display, you can use the system color picker to select and preview P3 colors, and to compare them with sRGB colors.

#### [System colors](/design/human-interface-guidelines/touch-bar#System-colors)

macOS offers a range of standard system colors that respond automatically to system white-point changes based on factors such as ambient light and keyboard backlight level.



| Color | API |
| --- | --- |
| Blue | [`systemBlue`](/documentation/appkit/nscolor/2879260-systemblue)
 |
| Brown | [`systemBrown`](/documentation/appkit/nscolor/2879266-systembrown)
 |
| Gray | [`systemGray`](/documentation/appkit/nscolor/2879265-systemgray)
 |
| Green | [`systemGreen`](/documentation/appkit/nscolor/2879264-systemgreen)
 |
| Orange | [`systemOrange`](/documentation/appkit/nscolor/2879263-systemorange)
 |
| Pink | [`systemPink`](/documentation/appkit/nscolor/2879261-systempink)
 |
| Purple | [`systemPurple`](/documentation/appkit/nscolor/2879259-systempurple)
 |
| Red | [`systemRed`](/documentation/appkit/nscolor/2879262-systemred)
 |
| Yellow | [`systemYellow`](/documentation/appkit/nscolor/2879267-systemyellow)
 |

**Don’t replicate system colors.** System color values may fluctuate from release to release and based on various environmental variables. Instead of trying to create custom colors that match the system colors, just use the system colors. For developer guidance, see [`NSColor`](/documentation/appkit/nscolor)
.

#### [Dynamic system colors](/design/human-interface-guidelines/touch-bar#Dynamic-system-colors)

macOS defines a range of system colors that dynamically match the color scheme of standard interface controls such as buttons and labels. The following system colors are ideal for use in the Touch Bar.



| Color | Description | API |
| --- | --- | --- |
| Control Color | The system color for the surface of a control. | [`controlColor`](/documentation/appkit/nscolor/1524856-controlcolor)
 |
| Label Color | The system color for the text of a label. | [`labelColor`](/documentation/appkit/nscolor/1534657-labelcolor)
 |
| Secondary Label Color | The system color for label text of lesser importance than text that uses labelColor. | [`secondaryLabelColor`](/documentation/appkit/nscolor/1533254-secondarylabelcolor)
 |
| Tertiary Label Color | The system color for label text of lesser importance than text that uses secondaryLabelColor. | [`tertiaryLabelColor`](/documentation/appkit/nscolor/1532376-tertiarylabelcolor)
 |
| Quaternary Label Color | The system color for label text of lesser importance than text that uses tertiaryLabelColor. | [`quaternaryLabelColor`](/documentation/appkit/nscolor/1534635-quaternarylabelcolor)
 |

### [Layout](/design/human-interface-guidelines/touch-bar#Layout)

The width of the Touch Bar display differs depending on the device.

![Screenshot of a Touch Bar second generation that indicates the overall area is 1004 points wide by 30 points tall.](https://docs-assets.developer.apple.com/published/3f15cffa68cc6c20f7826fa05d1a0c42/tb-b-layout-total@2x.png)Touch Bar (2nd generation)![Screenshot of a Touch Bar first generation that indicates the overall area is 1085 points wide by 30 points tall.](https://docs-assets.developer.apple.com/published/c8e4a3d2a713f7933b41ae1380be6395/tb-layout-total@2x.png)Touch Bar (1st generation)#### [Touch Bar areas](/design/human-interface-guidelines/touch-bar#Touch-Bar-areas)

In its standard configuration, the Touch Bar display consists of either two or three areas, depending on the device. The system enforces a 16 pt separation between areas.

The Touch Bar (2nd generation) display contains two areas: the app region and the Control Strip. Although the second generation Touch Bar doesn’t include a system button area, you can display a system button within your app region.

![Diagram of a Touch Bar second generation with callouts that show the locations and widths of the minimum app region and the maximum collapsed control strip, in addition to the two area separators.](https://docs-assets.developer.apple.com/published/6cbd7ba1f46a5272a4cf789edbf22ecd/tb-b-layout-regions@2x.png)

The Touch Bar (1st generation) display includes three areas: the system button area, the app region, and the Control Strip.

![Diagram of a Touch Bar first generation in which callouts show the locations and widths of the system button, the minimum app region, and the maximum collapsed control strip, in addition to the two area separators.](https://docs-assets.developer.apple.com/published/d1411173989cb45a2acb675b3dfe2571/tb-layout-regions@2x.png)



| Area | Contains | User configurable? |
| --- | --- | --- |
| Control Strip | System-level controls for performing actions, like initiating Siri or adjusting the volume level. | Yes. People can extend the Control Strip to the full width of the Touch Bar, collapse it to the right side of the Touch Bar, reduce it in size, or hide it entirely. By default, the Control Strip appears in its collapsed state and contains four controls. |
| App region | Your app’s controls. | Yes. People can hide this area entirely. When the Control Strip is visible, the app region has a minimum width of 685 pt. |
| System button (available on some models) | A contextually relevant button, like Esc, Cancel, or Done. | No. When present, this area’s width is 64 pt. In Touch Bar (2nd generation), you can use 8 pt spacing to display the relevant button in the app region, where it’s unavailable by default. |

**Assume that the default Control Strip is visible.** Although people can reconfigure the Control Strip, reduce its size, or hide it completely, don’t rely on the availability of this space for your design.

#### [Positioning app controls](/design/human-interface-guidelines/touch-bar#Positioning-app-controls)

You have several options for adding visual separation between app controls in the Touch Bar.



| Spacing type | Width between controls |
| --- | --- |
| Default | 8 pt |
| Small fixed space | 16 pt |
| Large fixed space | 32 pt |
| Flexible space | Varies to match the available space. |

**Position controls logically and intuitively.** If your app offers a control that persists across different modalities, it can work well to put the control in the left side of the app region. For example, the Compose button in Notes always appears in the far left of the Touch Bar, regardless of whether people are navigating notes, editing a note, or browsing attachments. On the other hand, primary controls that command people’s attention — such as an alert or the suggested items in the QuickType bar — work best centered in the app region, with secondary options on the left. Consider using the order of controls in your app’s toolbar to inform the order of Touch Bar controls in the app region. When you use consistent control positions in both areas, people can rely on their familiarity with your onscreen controls to help them use your Touch Bar controls.

Important

If the order of your Touch Bar controls mirrors the order of controls in your app’s window, make sure to adjust the control order in the app region when your app uses a right-to-left layout.

**Construct a flexible layout.** The app region varies in width depending on the configuration of the Control Strip and the device, so consider allowing certain controls — such as sliders and scrubbers — to stretch when additional space becomes available. **Strive for consistent spacing.** As much as possible, make controls in the Touch Bar equidistant, except when spacing variations are necessary for clarity or to cluster related controls. **Use flexible spaces and grouping to aid alignment.** Flexible space between items pushes the items on the left toward the left side of the Touch Bar and the items on the right toward the right side of the Touch Bar. Grouping lets you position multiple controls at once. For example, you can center a control or group by marking it as the principal item in the Touch Bar. **Avoid repositioning controls automatically.** People can become frustrated and confused if a control changes position by itself. If it makes sense in your app, consider letting people customize control positioning. **Avoid manually reversing controls in right-to-left locales.** The system already reverses certain controls, such as segmented controls and sliders. Manually reversing controls can cause problems with Touch Bar customization features.

For developer guidance, see [`NSTouchBarItem`](/documentation/appkit/nstouchbaritem)
.

#### [Common layout styles](/design/human-interface-guidelines/touch-bar#Common-layout-styles)

Touch Bar layouts can vary significantly from app to app because of factors like configuration options, various control sizes, and the device your app is running on. When possible, use one of the following common layout styles for your controls.

**Layout with one principal item.** The center of the Touch Bar contains a single large control, such as a [candidate list](https://developer.apple.com/design/human-interface-guidelines/touch-bar#Candidate-lists)
. Additional controls, such as buttons and segmented controls, are on the left. In Touch Bar (2nd generation), layouts with one principal item can look like this:

![Diagram of a Touch Bar second generation in which callouts show the layout of a two-segment segmented control, one button, and a candidate list in the app region. Each segment measures 75.5 points wide, the button measures 72 points wide, and the candidate list can range from 389 to 445 points wide. There is a one point space between the segments, and an eight point space on both sides of the button.](https://docs-assets.developer.apple.com/published/46e4851eac65e72b66b00a4aa5dc73e5/tb-b-layout-1principal1@2x.png)

![Diagram of a Touch Bar second generation in which callouts show the layout of three buttons and a candidate list in the app region. Each button measures 72 points wide and the candidate list can range from 389 to 445 points wide. There is an eight point space between each of the buttons and also between the rightmost button and the candidate list.](https://docs-assets.developer.apple.com/published/9398e30ef520a150e3e6d6104abd8741/tb-b-layout-1principal2@2x.png)

![Diagram of a Touch Bar second generation in which callouts show the layout of a three-segment segmented control and a candidate list in the app region. Two segments measure 63.5 points wide, the middle segment measures 63 points wide, and the candidate list can range from 389 to 445 points wide. There is a one point space on both sides of the middle segment and a space that can range between 48 and 104 points between the segmented controls and the candidate list.](https://docs-assets.developer.apple.com/published/9952e600008750aecd2678f865683c22/tb-b-layout-1principal3@2x.png)

Note

In Touch Bar (2nd generation), a principal candidate list control typically remains centered with respect to the device, whereas other types of principal controls may appear off-center in some circumstances. For example, an item might be too large to center in the current configuration, but may become centered when people customize the Control Strip.

In Touch Bar (1st generation), layouts with one principal item can look like this:

![Diagram of a Touch Bar first generation in which callouts show the layout of a two-segment segmented control, one button, and a candidate list in the app region. Each segment measures 75.5 points wide, the button measures 72 points wide, and the candidate list measures 445 points wide. There is a one point space between the segments, and an eight point space on both sides of the button.](https://docs-assets.developer.apple.com/published/9d81a35c4070087e2efe8f3511feef6f/tb-layout-1principal1@2x.png)

![Diagram of a Touch Bar first generation in which callouts show the layout of three buttons and a candidate list in the app region. Each button measures 72 points wide and the candidate list measures 445 points wide. There is an eight point space between each of the buttons and also between the rightmost button and the candidate list.](https://docs-assets.developer.apple.com/published/9690f2e9631b9ea182268c0272298b57/tb-layout-1principal2@2x.png)

![Diagram of a Touch Bar first generation in which callouts show the layout of a three-segment segmented control and a candidate list in the app region. Two segments measure 63.5 points wide, the middle segment measures 63 points wide, and the candidate list measures 445 points wide. There is a one point space on both sides of the middle segment and a space that can range between 48 and 104 points between the segmented controls and the candidate list.](https://docs-assets.developer.apple.com/published/28a3a525be4fc485aaa9e76360e90038/tb-layout-1principal3@2x.png)

**Layout with two principal items.** The center of the Touch Bar contains two consistently sized controls. Additional controls are on the left.

In Touch Bar (2nd generation), a layout with two principal items can look like this:

![Diagram of a Touch Bar second generation in which callouts show the layout of a three-segment segmented control and two buttons in the app region. Two segments measure 63.5 points wide, the middle segment measures 63 points wide, and each button measures 143 points wide. There are one point spaces between the segments and an eight point space between the buttons.](https://docs-assets.developer.apple.com/published/d913d81251ce22e2c19cd0d6aceab856/tb-b-layout-2principal@2x.png)

In Touch Bar (1st generation), a layout with two principal items can look like this:

![Diagram of a Touch Bar first generation in which callouts show the layout of a three-segment segmented control and two buttons in the app region. Two segments measure 63.5 points wide, the middle segment measures 63 points wide, and each button measures 143 points wide. There are one point spaces between the segments and an eight point space between the buttons.](https://docs-assets.developer.apple.com/published/9d1b46ce96c0de9047894adb8234c68f/tb-layout-2principal@2x.png)

**Layout with three principal items.** The center of the Touch Bar contains three consistently sized controls. Additional controls are on the left.

In Touch Bar (2nd generation), a layout with three principal items can look like this:

![Diagram of a Touch Bar second generation in which callouts show the layout of six buttons in the app region. From the left, the first three buttons each measure 72 points wide and the last three buttons each measure 143 points wide. All spaces between buttons measure eight points wide.](https://docs-assets.developer.apple.com/published/f0e515398d127d00b5f03c17d862c7d8/tb-b-layout-3principal@2x.png)

In Touch Bar (1st generation), a layout with three principal items can look like this:

![Diagram of a Touch Bar first generation in which callouts show the layout of six buttons in the app region. From the left, the first three buttons each measure 72 points wide and the last three buttons each measure 143 points wide. All spaces between buttons measure eight points wide.](https://docs-assets.developer.apple.com/published/ffc4fc07d2e38e7f0627701abcbcef00/tb-layout-3principal@2x.png)

**Fluid layout.** This layout includes consistently-sized controls, such as buttons.

In Touch Bar (2nd generation), a fluid layout can look like this:

![Diagram of a Touch Bar second generation in which callouts show the layout of eight buttons in the app region. Each button measures 144 pixels wide and between each button is a flexible spacer.](https://docs-assets.developer.apple.com/published/9f94ccfcb2029c4682f6e4dd83c79558/tb-b-layout-fluid@2x.png)

In Touch Bar (1st generation), a fluid layout can look like this:

![Diagram of a Touch Bar first generation in which callouts show the layout of eight buttons in the app region. Each button measures 144 pixels wide and between each button is a flexible spacer.](https://docs-assets.developer.apple.com/published/83a2d425aa7894e8c7f50e678b77cd06/tb-layout-fluid@2x.png)

### [Typography](/design/human-interface-guidelines/touch-bar#Typography)

The Touch Bar uses a variant of San Francisco, the system font in macOS. Standard Touch Bar controls, such as buttons and segmented controls, automatically use this variant. For guidance, see [Typography](/design/human-interface-guidelines/typography)
; for developer guidance, see [`NSFont`](/documentation/appkit/nsfont)
.

[Interface icons](/design/human-interface-guidelines/touch-bar#Interface-icons)
-------------------------------------------------------------------------------

macOS provides many interface icons you can use to represent common tasks and types of content in your app’s Touch Bar controls.

When you use AppKit API to display a system-provided glyph, you automatically get an image in the format that’s appropriate for the version of macOS in which your app is running. For example, if your app runs in macOS 11 and later, you get [SF Symbols](/design/human-interface-guidelines/sf-symbols)
; if your app runs in Catalina or earlier, AppKit continues to provide the existing template image. For developer guidance, see [`NSTouchBarItem`](/documentation/appkit/nstouchbaritem)
.

Important

By default, the system APIs return SF Symbols configured as 13 pt, large scale, and medium weight.

In some cases, a symbol might not have the same size or alignment as the image it replaces, so it’s important to check your layout.

**Prefer system images because people are familiar with them.** Also, system-provided glyphs automatically receive appropriate coloring, respond to system white-point changes based on factors such as ambient light and keyboard backlight level, and respond to user interactions.

**Use each system-defined glyph according to its meaning — not its appearance.** When you choose an image for its meaning, your app can remain visually consistent with the system even if the appearance of the image changes.

**Use only system images that are designed for the Touch Bar.** Don’t use other types of images in the Touch Bar, such as toolbar glyphs.

**Design a custom symbol or image if you can’t find a system-defined one that meets your needs.** Designing a custom symbol or image lets you communicate unique details that help people use your app; repurposing a system-defined image can cause confusion. For guidance, see [Custom Touch Bar icons](/design/human-interface-guidelines/touch-bar#Custom-Touch-Bar-icons)
; for general design guidance, see [Icons](/design/human-interface-guidelines/icons)
.

Note

Some system icons, like Go Back and Go Forward, automatically reverse direction in right-to-left locales.



| Image (Catalina and earlier) | SF Symbol (macOS 11 and later) | Meaning |
| --- | --- | --- |
| A white plus sign within a black disk. [`touchBarAddDetailTemplateName`](/documentation/appkit/nsimage/2647000-touchbaradddetailtemplatename)
 |  plus.circle | Displays additional detail for an item. |
| A plus sign. [`touchBarAddTemplateName`](/documentation/appkit/nsimage/2544735-touchbaraddtemplatename)
 |  plus | Creates a new item. |
| An alarm clock with its hands at 9:00. [`touchBarAlarmTemplateName`](/documentation/appkit/nsimage/2646938-touchbaralarmtemplatename)
 |  alarm | Sets or displays an alarm. |
| A freestanding microphone with a slash through it. [`touchBarAudioInputMuteTemplateName`](/documentation/appkit/nsimage/2646941-touchbaraudioinputmutetemplatena)
 |  mic.slash | Mutes audio input or denotes that audio input is muted. |
| A freestanding microphone. [`touchBarAudioInputTemplateName`](/documentation/appkit/nsimage/2646933-touchbaraudioinputtemplatename)
 |  mic | Denotes audio input. |
| A right-facing speaker with 3 concentric curved lines representing sound waves. On top of the image is a slash from top left to bottom right. [`touchBarAudioOutputMuteTemplateName`](/documentation/appkit/nsimage/2646959-touchbaraudiooutputmutetemplaten)
 |  speaker.slash.fill | Mutes audio output or denotes that audio output is muted. |
| A right-facing speaker with 3 concentric curved lines representing sound waves. [`touchBarAudioOutputVolumeHighTemplateName`](/documentation/appkit/nsimage/2646973-touchbaraudiooutputvolumehightem)
 |  speaker.wave.3.fill | Sets the audio output volume to high or denotes that the audio output volume is set to high. |
| A right-facing speaker with 3 concentric curved lines representing sound waves. The outermost 2 waves are gray; the inner wave is black. [`touchBarAudioOutputVolumeLowTemplateName`](/documentation/appkit/nsimage/2646925-touchbaraudiooutputvolumelowtemp)
 |  speaker.wave.1.fill | Sets the audio output volume to low or denotes that the audio output volume is set to low. |
| A right-facing speaker with 3 concentric curved lines representing sound waves. The outermost wave is gray; the inner 2 waves are black. [`touchBarAudioOutputVolumeMediumTemplateName`](/documentation/appkit/nsimage/2646957-touchbaraudiooutputvolumemediumt)
 |  speaker.wave.2.fill | Sets the audio output volume to medium or denotes that the audio output volume is set to medium. |
| A right-facing speaker with 3 gray concentric curved lines representing sound waves. [`touchBarAudioOutputVolumeOffTemplateName`](/documentation/appkit/nsimage/2646988-touchbaraudiooutputvolumeofftemp)
 |  speaker.fill | Turns off audio output or denotes that audio output is turned off. |
| An open book. [`touchBarBookmarksTemplateName`](/documentation/appkit/nsimage/2646985-touchbarbookmarkstemplatename)
 |  book | Shows app-specific bookmarks. |
| A disk filled with wedges of rainbow colors. [`touchBarColorPickerFillName`](/documentation/appkit/nsimage/2646978-touchbarcolorpickerfillname)
 | – | Shows a color picker so people can select a fill color. |
| The letter A filled with rainbow colors. [`touchBarColorPickerFontName`](/documentation/appkit/nsimage/2646992-touchbarcolorpickerfontname)
 | – | Shows a color picker so people can select a text color. |
| A circle drawn with a stroke filled with rainbow colors. [`touchBarColorPickerStrokeName`](/documentation/appkit/nsimage/2646961-touchbarcolorpickerstrokename)
 | – | Shows a color picker so people can select a stroke color. |
| A solid black phone receiver. [`touchBarCommunicationAudioTemplateName`](/documentation/appkit/nsimage/2646979-touchbarcommunicationaudiotempla)
 |  phone | Initiates or denotes audio communication. |
| A solid black video camera. [`touchBarCommunicationVideoTemplateName`](/documentation/appkit/nsimage/2646932-touchbarcommunicationvideotempla)
 |  video | Initiates or denotes video communication. |
| An outlined square with a black pencil on top that goes from above the top-right corner to near the middle of the square. [`touchBarComposeTemplateName`](/documentation/appkit/nsimage/2544716-touchbarcomposetemplatename)
 |  square.and.pencil | Opens a new document or view in edit mode. |
| An outlined trash can. [`touchBarDeleteTemplateName`](/documentation/appkit/nsimage/2646939-touchbardeletetemplatename)
 |  trash | Deletes the current or selected item. |
| A white downward-pointing arrow within a black disk. [`touchBarDownloadTemplateName`](/documentation/appkit/nsimage/2646924-touchbardownloadtemplatename)
 |  arrow.down.circle | Downloads an item. |
| Two black arrows pointing away from each other. One arrow points to the bottom left and the other points to the top right. [`touchBarEnterFullScreenTemplateName`](/documentation/appkit/nsimage/2646946-touchbarenterfullscreentemplaten)
 |  arrow.up.left.and.arrow.down.right | Enters full screen mode. |
| Two black arrows pointing toward each other. One arrow points from the top right and the other points from the bottom left. [`touchBarExitFullScreenTemplateName`](/documentation/appkit/nsimage/2646983-touchbarexitfullscreentemplatena)
 |  arrow.down.right.and.arrow.up.left | Exits full screen mode. |
| Two black triangles both pointing right. [`touchBarFastForwardTemplateName`](/documentation/appkit/nsimage/2646994-touchbarfastforwardtemplatename)
 |  forward.fill | Fast-forwards through media playback or slides. |
| A black folder with a white square containing a black plus sign in the bottom-left corner. [`touchBarFolderCopyToTemplateName`](/documentation/appkit/nsimage/2646998-touchbarfoldercopytotemplatename)
 |  plus.rectangle.on.folder | Copies an item to a destination. |
| A black folder with a downward-pointing arrow on top of it. [`touchBarFolderMoveToTemplateName`](/documentation/appkit/nsimage/2646996-touchbarfoldermovetotemplatename)
 |  folder | Moves an item to a new destination. |
| A black folder. [`touchBarFolderTemplateName`](/documentation/appkit/nsimage/2646980-touchbarfoldertemplatename)
 |  folder | Opens or represents a folder. |
| A black, lowercase letter I within a black circle. [`touchBarGetInfoTemplateName`](/documentation/appkit/nsimage/2646951-touchbargetinfotemplatename)
 |  info.circle | Displays additional information about an item. |
| A left-pointing chevron. [`touchBarGoBackTemplateName`](/documentation/appkit/nsimage/2544848-touchbargobacktemplatename)
 |  chevron.backward | Returns to the previous screen or location. |
| A downward-pointing chevron. [`touchBarGoDownTemplateName`](/documentation/appkit/nsimage/2646945-touchbargodowntemplatename)
 |  chevron.down | Moves to the next vertical item. |
| A right-pointing chevron. [`touchBarGoForwardTemplateName`](/documentation/appkit/nsimage/2544734-touchbargoforwardtemplatename)
 |  chevron.forward | Moves to the next screen or location. |
| An upward-pointing chevron. [`touchBarGoUpTemplateName`](/documentation/appkit/nsimage/2646975-touchbargouptemplatename)
 |  chevron.up | Moves to the previous vertical item. |
| A clock that displays the time 9:00. [`touchBarHistoryTemplateName`](/documentation/appkit/nsimage/2646929-touchbarhistorytemplatename)
 |  clock | Displays historical information, such as recent downloads. |
| Two rows of three empty squares, each outlined in black. [`touchBarIconViewTemplateName`](/documentation/appkit/nsimage/2646943-touchbariconviewtemplatename)
 |  square.grid.2x2 | Displays items in an icon view. |
| A stack of four horizontal black lines. [`touchBarListViewTemplateName`](/documentation/appkit/nsimage/2646954-touchbarlistviewtemplatename)
 |  list.bullet | Displays items in a list view. |
| A closed black envelope with the flap outlined in white. [`touchBarMailTemplateName`](/documentation/appkit/nsimage/2646969-touchbarmailtemplatename)
 |  envelope | Creates an email message. |
| A black folder with a plus sign in the top-right corner. [`touchBarNewFolderTemplateName`](/documentation/appkit/nsimage/2646989-touchbarnewfoldertemplatename)
 |  folder.badge.plus | Creates a new folder. |
| A black message bubble. [`touchBarNewMessageTemplateName`](/documentation/appkit/nsimage/2646953-touchbarnewmessagetemplatename)
 |  message | Creates a new message or denotes the use of messaging. |
| A black compass needle pointing to north-east within a circle outlined in black. [`touchBarOpenInBrowserTemplateName`](/documentation/appkit/nsimage/2646990-touchbaropeninbrowsertemplatenam)
 |  safari | Opens an item in the browser. |
| Two vertical, parallel black bars. [`touchBarPauseTemplateName`](/documentation/appkit/nsimage/2646970-touchbarpausetemplatename)
 |  pause.fill | Pauses media playback or slides. Always store the current location when pausing, so playback can resume later. |
| A black, right-pointing triangle with two vertical parallel black bars on the right. [`touchBarPlayPauseTemplateName`](/documentation/appkit/nsimage/2646991-touchbarplaypausetemplatename)
 |  playpause.fill | Toggles between playing and pausing media or slides. |
| A black right-pointing triangle. [`touchBarPlayTemplateName`](/documentation/appkit/nsimage/2646967-touchbarplaytemplatename)
 |  play.fill | Begins or resumes media playback or slides. |
| A black eye shape with a white circle within it. [`touchBarQuickLookTemplateName`](/documentation/appkit/nsimage/2646952-touchbarquicklooktemplatename)
 |  eye | Opens an item in Quick Look. |
| A black disk. [`touchBarRecordStartTemplateName`](/documentation/appkit/nsimage/2646981-touchbarrecordstarttemplatename)
 |  circle.fill | Begins recording. |
| A black square. [`touchBarRecordStopTemplateName`](/documentation/appkit/nsimage/2646993-touchbarrecordstoptemplatename)
 |  stop.fill | Stops recording or stops media playback or slides. |
| A curved arrow indicating the clockwise direction. [`touchBarRefreshTemplateName`](/documentation/appkit/nsimage/2646995-touchbarrefreshtemplatename)
 |  arrow.clockwise | Moves backwards through media playback or slides. |
| Two black triangles both pointing left. [`touchBarRewindTemplateName`](/documentation/appkit/nsimage/2646950-touchbarrewindtemplatename)
 |  backward.fill | Moves backwards through media playback or slides. |
| A rectangle outlined in black with a curved, left-pointing arrow over the top-right corner. [`touchBarRotateLeftTemplateName`](/documentation/appkit/nsimage/2646972-touchbarrotatelefttemplatename)
 |  rotate.left | Moves to the next vertical item. |
| A rectangle outlined in black with a curved, right-pointing arrow over the top-left corner. [`touchBarRotateRightTemplateName`](/documentation/appkit/nsimage/2646977-touchbarrotaterighttemplatename)
 |  rotate.right | Rotates an item to the right. |
| A magnifying glass outlined in black, slanting to the left. [`touchBarSearchTemplateName`](/documentation/appkit/nsimage/2647001-touchbarsearchtemplatename)
 |  magnifyingglass | Displays a search field or initiates a search. |
| A square outlined in black with a black arrow pointing up from near the top edge. [`touchBarShareTemplateName`](/documentation/appkit/nsimage/2646948-touchbarsharetemplatename)
 |  square.and.arrow.up | Shares content with others or to social media. |
| A black-outlined rectangle divided by a vertical line about 40 percent from the left. Within the left side are a stack of three short, horizontal lines. [`touchBarSidebarTemplateName`](/documentation/appkit/nsimage/2646966-touchbarsidebartemplatename)
 |  sidebar.leading | Displays a sidebar in the current view. |
| The number 15 circled by a black double-headed arrow pointing right in a clockwise direction. [`touchBarSkipAhead15SecondsTemplateName`](/documentation/appkit/nsimage/2646930-touchbarskipahead15secondstempla)
 |  goforward.15 | Skips 15 seconds ahead during media playback. |
| The number 30 circled by a black double-headed arrow pointing right in a clockwise direction. [`touchBarSkipAhead30SecondsTemplateName`](/documentation/appkit/nsimage/2646927-touchbarskipahead30secondstempla)
 |  goforward.30 | Skips 30 seconds ahead during media playback. |
| Two black right-pointing triangles with a black vertical line at the point of the rightmost triangle. [`touchBarSkipAheadTemplateName`](/documentation/appkit/nsimage/2646974-touchbarskipaheadtemplatename)
 |  forward.end.alt.fill | Skips to the next chapter or location during media playback. |
| The number 15 circled by a black double-headed arrow pointing left in a counter clockwise direction. [`touchBarSkipBack15SecondsTemplateName`](/documentation/appkit/nsimage/2646934-touchbarskipback15secondstemplat)
 |  gobackward.15 | Skips 15 seconds back during media playback. |
| The number 30 circled by a double-headed black arrow pointing left in a counter clockwise direction. [`touchBarSkipBack30SecondsTemplateName`](/documentation/appkit/nsimage/2646976-touchbarskipback30secondstemplat)
 |  gobackward.30 | Skips 30 seconds back during media playback. |
| Two black left-pointing triangles with a black vertical line at the point of the leftmost triangle. [`touchBarSkipBackTemplateName`](/documentation/appkit/nsimage/2646944-touchbarskipbacktemplatename)
 |  backward.end.alt.fill | Skips to the previous chapter or location during media playback. |
| A black right-pointing triangle with a vertical black line at the point. [`touchBarSkipToEndTemplateName`](/documentation/appkit/nsimage/2646956-touchbarskiptoendtemplatename)
 |  forward.end.fill | Skips to the end during media playback. |
| A black left-pointing triangle with a vertical black line at the point. [`touchBarSkipToStartTemplateName`](/documentation/appkit/nsimage/2646968-touchbarskiptostarttemplatename)
 |  backward.end.fill | Skips to the start during media playback. |
| A black right-pointing triangle within a black-outlined rectangle. [`touchBarSlideshowTemplateName`](/documentation/appkit/nsimage/2646935-touchbarslideshowtemplatename)
 |  play.rectangle | Starts a slideshow. |
| A tag outlined in black, pointing left. [`touchBarTagIconTemplateName`](/documentation/appkit/nsimage/2646958-touchbartagicontemplatename)
 |  tag | Applies a tag to an item. |
| The capital letter B drawn in a thick black stroke. [`touchBarTextBoldTemplateName`](/documentation/appkit/nsimage/2646964-touchbartextboldtemplatename)
 |  bold | Makes text bold. |
| A capital letter T within a square outlined in black. A black dot is at the center of both vertical sides of the square. [`touchBarTextBoxTemplateName`](/documentation/appkit/nsimage/2646963-touchbartextboxtemplatename)
 |  textbox | Inserts a text box. |
| A stack of four horizontal black lines. From the top, the first and third are one length and the second and fourth are a shorter length. The midpoint of each line is at the same horizontal position. [`touchBarTextCenterAlignTemplateName`](/documentation/appkit/nsimage/2646940-touchbartextcenteraligntemplaten)
 |  text.aligncenter | Center aligns text. |
| A black capital letter I slanted slightly to the right. [`touchBarTextItalicTemplateName`](/documentation/appkit/nsimage/2646942-touchbartextitalictemplatename)
 |  italic | Italicizes text. |
| A stack of four horizontal black lines all the same length. [`touchBarTextJustifiedAlignTemplateName`](/documentation/appkit/nsimage/2646962-touchbartextjustifiedaligntempla)
 |  text.justify | Justifies text, aligning it to both the left and right. |
| A stack of four horizontal black lines. From the top, the first and third are one length, the second and fourth are a shorter length. All four lines start from the same horizontal position on the left. [`touchBarTextLeftAlignTemplateName`](/documentation/appkit/nsimage/2646937-touchbartextleftaligntemplatenam)
 |  text.alignleft | Left-aligns text. |
| A stack of four horizontal lines of the same length, each with a black bullet on the left. [`touchBarTextListTemplateName`](/documentation/appkit/nsimage/2646960-touchbartextlisttemplatename)
 |  list.bullet | Inserts a list or converts text to list form. |
| A stack of four horizontal black lines. From the top, the first and third are one length, the second and fourth are a shorter length. All four lines start from the same horizontal position on the right. [`touchBarTextRightAlignTemplateName`](/documentation/appkit/nsimage/2646999-touchbartextrightaligntemplatena)
 |  text.alignright | Right-aligns text. |
| A capital letter S with a short horizontal line through the middle. [`touchBarTextStrikethroughTemplateName`](/documentation/appkit/nsimage/2646986-touchbartextstrikethroughtemplat)
 |  strikethrough | Applies a strikethrough to text. |
| A capital letter U sitting on a short horizontal line. [`touchBarTextUnderlineTemplateName`](/documentation/appkit/nsimage/2646947-touchbartextunderlinetemplatenam)
 |  underline | Underlines text. |
| The silhouette of a person’s head and shoulders within a circle. A small plus sign is on the right side of the silhouette. [`touchBarUserAddTemplateName`](/documentation/appkit/nsimage/2646936-touchbaruseraddtemplatename)
 |  person.crop.circle.badge.plus | Creates a new user. |
| The silhouettes of two people, heads and shoulders only. The person on the right is slightly in front of the person on the left. [`touchBarUserGroupTemplateName`](/documentation/appkit/nsimage/2646984-touchbarusergrouptemplatename)
 |  person.2.fill | Shows or represents information about a group of users. |
| The silhouette of a person’s head and shoulders. [`touchBarUserTemplateName`](/documentation/appkit/nsimage/2646949-touchbarusertemplatename)
 |  person.fill | Shows or represents information about a user. |
| A right-pointing speaker with one curved line on the right side, representing a sound wave. [`touchBarVolumeDownTemplateName`](/documentation/appkit/nsimage/2646928-touchbarvolumedowntemplatename)
 |  speaker.wave.1.fill | Decreases the volume. |
| A right-pointing speaker with two curved lines on the right side, representing sound waves. [`touchBarVolumeUpTemplateName`](/documentation/appkit/nsimage/2646987-touchbarvolumeuptemplatename)
 |  speaker.wave.3.fill | Increases the volume. |

### [Custom Touch Bar icons](/design/human-interface-guidelines/touch-bar#Custom-Touch-Bar-icons)

If your app includes tasks or modes that can’t be represented by a system-provided Touch Bar image, you can create your own. [Apple Design Resources](https://developer.apple.com/design/resources/#macos-apps)
 provides downloadable Photoshop and Sketch templates you can use to design properly scaled icons for the Touch Bar. For guidance, see [Icons](/design/human-interface-guidelines/icons)
.

In general, create icons that look similar to the icons on the physical keyboard keys. Supply high-resolution images with a scale factor of @2x for all artwork that appears in the Touch Bar. To learn about image resolutions, see [Resolution](/design/human-interface-guidelines/images#Resolution)
.

**Design recognizable icons that clearly relate to your app on the main screen.** If necessary, you can vary the images to match the style of the Touch Bar.

**Avoid icons that extend to the full height of the Touch Bar.** In general, create icons that are no taller than 44 px (36 px for circular icons).



|  |  |
| --- | --- |
| **Ideal icon size** | 18x18 pt (36x36 px @2x) |
| **Maximum icon size** | 22x22 pt (44x44 px @2x) |

![A row of six example icons, each of which has squares drawn around it, showing how it fits within areas that measure 36 pixels square and 44 pixels square.](https://docs-assets.developer.apple.com/published/d1bb25de8adb1ae4423d50695c8639bd/tb-custom-icon-example@2x.png)

**Keep icons optically centered.** Crop artwork to match the icon’s width, then add padding as needed to keep the icon optically centered when it’s displayed in a control.

**Prefer a 45-degree angle for diagonal elements.** Using the same angle as in system icons like [`touchBarAudioInputMuteTemplateName`](/documentation/appkit/nsimage/2646941-touchbaraudioinputmutetemplatena)
 and [`touchBarComposeTemplateName`](/documentation/appkit/nsimage/2544716-touchbarcomposetemplatename)
 helps your custom icons look at home in the Touch Bar.

**Avoid using color to communicate on and off states.** The system already changes the background appearance of standard controls that are in an off state.

**Give most icons a 100% opacity fill.** To optimize readability, you might want to use a 70% opacity fill in combination with a 100% opacity fill. Use midtones only for improving readability and balance.

For guidance, see [Color](/design/human-interface-guidelines/touch-bar#Color)
.

**To match the style of the physical keyboard, give most icons a 2 px stroke.** If your design requires more visual weight, consider a 3 px stroke.

**As much as possible, match the corner styles of the system images.** For example, use square corners for icons with a 2 px stroke, rounded corners with a 1px radius for icons with a 3 px stroke, and rounded corners with a 4 px radius for solid shapes.

[Controls and views](/design/human-interface-guidelines/touch-bar#Controls-and-views)
-------------------------------------------------------------------------------------

The system offers a range of standard controls you can provide in the app region of the Touch Bar. For consistency, use these controls when possible.

### [Buttons](/design/human-interface-guidelines/touch-bar#Buttons)

Buttons initiate app-specific actions, and can include an icon and a title.

![Partial screenshot of a Touch Bar in which a file button is highlighted.](https://docs-assets.developer.apple.com/published/32d43345c9a4e17d38ee7943034ddc2e/tb-cv-buttons@2x.png)

**Prefer icons over titles.** Strive to design clear icons that stand on their own without supporting text.

**Keep titles short.** Lengthy titles can crowd the Touch Bar.

**Customize a button’s bezel color if necessary.** The system-provided button bezel looks similar to the physical keyboard buttons and contributes to a unified visual experience. If your app requires a custom bezel color, consider using a dark color, which tends to look good in the Touch Bar.

For guidance, see [Buttons](/design/human-interface-guidelines/buttons)
. For developer guidance, see [`NSButton`](/documentation/appkit/nsbutton)
.

#### [Toggles](/design/human-interface-guidelines/touch-bar#Toggles)

A toggle switches between on and off states.

![Partial screenshot of a Touch Bar that highlights a toggle button in the on state.](https://docs-assets.developer.apple.com/published/dcbcbf724fc6dde4d1d770f1ca1c193e/tb-cv-toggle-on@2x.png)On![Partial screenshot of a Touch Bar that highlights a toggle button in the off state.](https://docs-assets.developer.apple.com/published/7844cccb1e835013878e13ec21ad806a/tb-cv-toggle-off@2x.png)Off**Let the background indicate a toggle’s state.** The system automatically changes the background appearance of buttons in an off state, so there’s no need to indicate the state using color, text, or a different icon.

**Use toggles in place of checkboxes and radio buttons.** If you need a control that lets people choose between two states, use a toggle button.

For developer guidance, see the [`state`](/documentation/appkit/nsbutton/1528907-state)
 property of [`NSButton`](/documentation/appkit/nsbutton)
.

### [Candidate lists](/design/human-interface-guidelines/touch-bar#Candidate-lists)

A candidate list offers autocompletion suggestions during text entry. People can tap a suggestion to accept and insert it into the active text field or text view on the main screen. People can also expand or collapse a candidate list. An expanded candidate list replaces other controls that reside within the expansion area.

![Screenshot of a Touch Bar that suggests the terms quick, quickly, and Quick in a candidate list.](https://docs-assets.developer.apple.com/published/e365ceb30b1f23779e99dc2c7b5b33d0/tb-cv-candidate-list@2x.png)

For developer guidance, see [`NSCandidateListTouchBarItem`](/documentation/appkit/nscandidatelisttouchbaritem)
.

### [Character pickers](/design/human-interface-guidelines/touch-bar#Character-pickers)

A character picker opens a popover that includes a list of special characters, such as emoji. People can tap a character in the picker to insert it into the active text area on the main screen.

![Partial screenshot of a Touch Bar that highlights a character picker that’s collapsed.](https://docs-assets.developer.apple.com/published/a816d16db55cf4b0c6992f03078e4956/tb-cv-character-picker-collapsed@2x.png)Closed![Partial screenshot of a Touch Bar that highlights a character picker that’s expanded.](https://docs-assets.developer.apple.com/published/2685a55a41d329cecba7f53a1c771cf6/tb-cv-character-picker-expanded@2x.png)OpenFor developer guidance, see [`NSCandidateListTouchBarItem`](/documentation/appkit/nscandidatelisttouchbaritem)
.

### [Color pickers](/design/human-interface-guidelines/touch-bar#Color-pickers)

A color picker opens a popover that includes controls for selecting a color. You can configure a color picker to display an icon for a color picker, a stroke color picker, or a text color picker. Regardless of the icon, all color pickers display the same popover.

![Partial screenshot of a Touch Bar that highlights a color picker and a stroke color picker, both of which are collapsed.](https://docs-assets.developer.apple.com/published/42059c481e4c2402714340e81a08e104/tb-cv-color-picker-collapsed@2x.png)Closed![Screenshot of a Touch Bar that highlights a color picker that’s expanded.](https://docs-assets.developer.apple.com/published/1c5d20b6232122821f2bc7b2763084f5/tb-cv-color-picker-expanded@2x.png)Open**Use icons as intended.** Use the stroke color picker icon for selecting a stroke color. Use the text color picker icon for selecting a text color. For other color selection scenarios, use the color picker icon.

For developer guidance, see [`NSColorPickerTouchBarItem`](/documentation/appkit/nscolorpickertouchbaritem)
.

### [Labels](/design/human-interface-guidelines/touch-bar#Labels)

A label displays read-only text that doesn’t appear within a control.

**In general, avoid labels.** Although the Touch Bar can display labels, it’s generally best to avoid them because they’re not interactive. Instead, focus on designing meaningful icons for your controls. If you must include a label, keep it as short as possible.

**Prefer titles over labels when supplementing complex icons.** If the meaning of a control’s icon isn’t clear on its own, consider including a short title within the control to provide context.

![Partial screenshot of a Touch Bar in which two buttons are called out. One button displays a pin icon and uses the title \"Location.\" The other button displays a calendar icon and uses the title \"Time.\"](https://docs-assets.developer.apple.com/published/aaa0f4ad197ba971927a9938b6561901/tb-cv-buttons-with-titles@2x.png)

For guidance, see [Labels](/design/human-interface-guidelines/labels)
. For developer guidance, see [`NSTextField`](/documentation/appkit/nstextfield)
.

### [Popovers](/design/human-interface-guidelines/touch-bar#Popovers)

A closed popover looks like a single button in the Touch Bar.

![Partial screenshot of a Touch Bar that highlights a closed popover for viewing items in columns.](https://docs-assets.developer.apple.com/published/e48964f9ee3e9b001f64cd250c3ecba4/tb-cv-popover-closed@2x.png)Closed![Screenshot of a Touch Bar that highlights an open popover that contains buttons for sorting options.](https://docs-assets.developer.apple.com/published/5d046fefb72e687e53c781df1d4342f7/tb-cv-popover-open@2x.png)OpenWhen it’s open, the popover replaces the current set of controls in the app region with a modal overlay containing a transient set of controls. In this modal overlay, people make a selection or tap a close button to return to the collapsed state and the previous set of controls.

Tip

In Touch Bar (2nd generation), the popover’s close button appears within the app region; in Touch Bar (1st generation), the close button replaces the system button. The second generation Touch Bar decreases the space available for popovers by 64 points and the system may display controls closer together to avoid clipping controls.

Collapsed popovers open when people tap them. Optionally, popovers can also open in response to a touch and hold gesture. Popovers that support touch and hold include a trailing carat decoration.

![Partial screenshot of a Touch Bar that highlights a closed popover for viewing items in columns.](https://docs-assets.developer.apple.com/published/314da988367c83ea201fc1eff922a5b7/tb-cv-collapsed-popover-closed@2x.png)Closed![Screenshot of a Touch Bar that highlights an open popover that contains buttons for sorting options.](https://docs-assets.developer.apple.com/published/f152dceafdacc50e16eed80f4c3a02a4/tb-cv-collapsed-popover-open@2x.png)OpenA popover can present the same overlay regardless of the gesture people use to expand it, or it can present a different overlay for each gesture. In a touch and hold overlay, people make a selection by sliding their holding finger to a control, and collapse the popover by lifting their finger.

**Use popovers sparingly.** Prefer Touch Bar controls that perform an action with a single tap.

**Avoid nesting popovers.** In general, don’t require people to navigate more than one level in the Touch Bar.

**Reserve touch and hold for simple popovers.** Use touch and hold primarily to display an overlay that includes a simple set of options — such as a single segmented control — from which people can make a selection.

**Indicate choice selection in a collapsed popover.** When an expanded popover includes a list of options, show the currently selected option in the collapsed state.

**Provide an obvious exit path.** Make sure people always know how to collapse a popover and return to the previous set of controls.

For developer guidance, see [`NSPopoverTouchBarItem`](/documentation/appkit/nspopovertouchbaritem)
.

### [Scrubbers](/design/human-interface-guidelines/touch-bar#Scrubbers)

A scrubber lets people swipe left and right to navigate through content like a list of dates or a group of photos. Scrubbers can be fixed or free, and are highly customizable — but need to retain an appearance that doesn’t feel out of place in the Touch Bar.

For developer guidance, see [`NSScrubber`](/documentation/appkit/nsscrubber)
.

#### [Fixed scrubbers](/design/human-interface-guidelines/touch-bar#Fixed-scrubbers)

A fixed scrubber allows for fluid, continuous interaction with a set of arranged content, such as open Safari tabs. As people swipe across the scrubber, items beneath their finger become highlighted. Depending on the scrubber’s configuration, people make a selection by moving a finger to the item, or by lifting their finger from the scrubber. If the amount of content exceeds the size of a fixed scrubber, the scrubber automatically scrolls to reveal additional items as the finger nears the edge of the control. In a fixed scrubber, people use a finger to move the selection, rather than the content.

![Screenshot of a Touch Bar that highlights a fixed scrubber. The six items in the scrubber are six different Safari pages. The third item from the left is selected.](https://docs-assets.developer.apple.com/published/9e67256da4a516b4031cb59583aa376a/tb-cv-fixed-scrubber@2x.png)

#### [Free scrubbers](/design/human-interface-guidelines/touch-bar#Free-scrubbers)

A free scrubber presents content in a scrollable list — such as a list of Calendar dates — that people swipe to scroll. Depending on the scrubber’s configuration, people select an item by moving it to a specific location, like the center of the scrubber, or by tapping the item while the scrubber is stationary.

**Use predictable and logically ordered values.** When the scrollable list in a free scrubber is stationary, some values may be hidden. If the list displays items in a logical order that follows an obvious progression, people can predict the hidden values and move through the list quickly. When viewing a list of country or region names, for example, people are generally better at predicting hidden values in an alphabetized list than in a list ordered by population size.

**Keep lists of values as short as possible.** People can find it tedious to navigate long lists in the Touch Bar. If you have a large list of values, consider presenting it on the main screen instead of the Touch Bar, so people can use the keyboard or trackpad for navigation.

### [Segmented controls](/design/human-interface-guidelines/touch-bar#Segmented-controls)

A segmented control is a linear set of two or more segments, each of which functions as a button — usually configured as a toggle. Within the control, all segments are equal in width. Like buttons, segments can contain text and icons.

![Partial screenshot of a Touch Bar that highlights a text justification segmented control that contains four segments.](https://docs-assets.developer.apple.com/published/f152dceafdacc50e16eed80f4c3a02a4/tb-cv-segmented-controls@2x.png)

**Limit the number of segments to improve usability.** Wider segments are easier for people to tap.

**Prefer icons over titles.** Strive to design clear icons that stand on their own without requiring supporting text.

**Try to keep segment content size consistent.** Because segments match in width, it’s visually coherent if the content in the segments is also equal in length.

**Keep titles short.** Lengthy titles can crowd the Touch Bar.

**Prefer darker colors for bezel color changes.** The appearance of the system-provided bezel resembles physical keyboard buttons. If your app requires a custom bezel color, dark colors are recommended.

For developer guidance, see [`NSSegmentedControl`](/documentation/appkit/nssegmentedcontrol)
.

### [Sharing service pickers](/design/human-interface-guidelines/touch-bar#Sharing-service-pickers)

People use sharing service pickers to share text, images, and other content with apps, social media accounts, and other services. When people tap a sharing service picker, it displays a popover that contains sharing buttons.

![Partial screenshot of a Touch Bar that highlights a sharing service picker in a closed state.](https://docs-assets.developer.apple.com/published/fad03c9101cc3c16641e836ed124c2e4/tb-cv-sharing-picker-closed@2x.png)Closed![Partial screenshot of a Touch Bar that highlights a sharing service picker in an open state.](https://docs-assets.developer.apple.com/published/99591462b4f3eab1a579c96dc53b5b3d/tb-cv-sharing-picker-open@2x.png)Open**Present a sharing service picker only when there’s content to share.** If people haven’t selected text, images, or other sharable content, the sharing service picker needs to be unavailable.

For developer guidance, see [`NSSharingServicePicker`](/documentation/appkit/nssharingservicepicker)
.

### [Sliders](/design/human-interface-guidelines/touch-bar#Sliders)

A slider is a horizontal track with a control called a thumb, which people can slide to move between a minimum and maximum value, such as screen brightness level, or position during media playback. As a slider’s value changes, the portion of track between the minimum value and the thumb fills with color.

![Partial screenshot of a Touch Bar that highlights a sharing service picker in an open state.](https://docs-assets.developer.apple.com/published/82d9de0501fa09107e4bab1c528f1ea1/tb-cv-slider@2x.png)

**Customize a slider’s appearance to match your app and add value.** Consider coordinating a slider’s track color with your app’s color scheme.

**Consider using a stepper instead of a slider when space is tight.** If a slider’s values cover a limited range and it’s possible to move through them in discrete steps, it might make sense to use a stepper. For guidance, see [Steppers](/design/human-interface-guidelines/touch-bar#Steppers)
.

**Provide left and right icons that illustrate the meaning of the minimum and maximum values.** A slider that adjusts image size, for example, could show a small image icon on the left and a large image icon on the right.

For developer guidance, see [`NSSlider`](/documentation/appkit/nsslider)
.

### [Steppers](/design/human-interface-guidelines/touch-bar#Steppers)

Steppers provide a set of continuous — usually numeric — values from which people can choose. A stepper displays the current value centered between a decrementing control and an incrementing control. People tap the controls or swipe the current value left or right to change the value by an amount you specify.

![Partial screenshot of a Touch Bar that highlights a font-size stepper with a current value of 22 points.](https://docs-assets.developer.apple.com/published/9565a3385c551a7aa1d077d738146cc6/tb-cv-steppers@2x.png)

**Display the item’s current value in the center view.** By default, a stepper uses text to display the current value. You can use a formatter to style the text — for example, in a stepper that lets people choose dates, you might make today’s date red. In some cases, it might make sense to use images instead of text, but it can be tricky to create images that convey a logical progression from which people can predict the values that precede and follow the current value. For example, a stepper that controls the line weight of a marking tool could use a set of images that vary in thickness to help people understand the effect of incrementing and decrementing the value.

**Avoid using a stepper when people are likely to make large adjustments to an item’s value.** Because a stepper changes an item’s value by one discrete step per swipe or tap, people would have to swipe or tap a lot to make a large value change.

[Platform considerations](/design/human-interface-guidelines/touch-bar#Platform-considerations)
-----------------------------------------------------------------------------------------------

*Not supported in iOS, iPadOS, tvOS, visionOS, or watchOS.*

[Resources](/design/human-interface-guidelines/touch-bar#Resources)
-------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/touch-bar#Related)

[Feedback](/design/human-interface-guidelines/feedback)


#### [Developer documentation](/design/human-interface-guidelines/touch-bar#Developer-documentation)

[`NSTouchBar`](/documentation/appkit/nstouchbar)


