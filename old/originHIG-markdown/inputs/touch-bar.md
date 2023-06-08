# **[inputs] touch-bar**

## The Touch Bar is a Retina display and input device located above the keyboard on supported MacBook Pro models.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-touch-bar-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-touch-bar-intro_2x.png)

Dynamic controls in the Touch Bar let people interact with content on the main screen and offer quick access to system-level and app-specific functionality based on the current context. For example, when people type text in a document, the Touch Bar could include controls for adjusting the font style and size. Or when viewing a location on a map, the Touch Bar could offer quick, one-tap access to nearby points of interest.

The following guidelines can help you provide a Touch Bar experience that people appreciate. For developer guidance, see [NSTouchBar](https://developer.apple.com/documentation/appkit/nstouchbar) and [Xcode Help](https://help.apple.com/xcode).

A Touch ID sensor to the right of the Touch Bar supports fingerprint authentication for logging into the computer and approving App Store and Apple Pay purchases. On devices that include the Touch Bar (2nd generation), a physical Esc (Escape) key appears to the left of the Touch Bar.

By default, the right side of the Touch Bar displays an expandable region called the *Control Strip* that includes controls for performing system-level tasks such as invoking Siri, adjusting the brightness of the main display, and changing the volume. You can place app-specific controls in the *app region*to the left of the Control Strip. In Touch Bar (1st generation), an Esc button or other system-provided button may appear to the left of the app region, depending on the context.

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-overview_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-overview_2x.png)

Touch Bar (2nd generation)

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-overview_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-overview_2x.png)

Touch Bar (1st generation)

People can configure the Touch Bar to suit their needs. For example, people can remove items from, or hide the Control Strip completely, in which case only the controls in the app region and the system button remain. Alternatively, people can hide the app region to view an expanded Control Strip.

You can support additional customization within the app region by letting people add and remove items.

**In general, let people customize your app’s Touch Bar experience.**Provide reasonable defaults for important and commonly used functions, but let people make adjustments to support their individual working styles.

**Provide alternative text labels for your Touch Bar controls.** By providing alternative text for your controls in the Touch Bar, VoiceOver can audibly describe the controls, making navigation easier for people with visual disabilities (for guidance, see [Accessibility](https://developer.apple.com/design/human-interface-guidelines/foundations/accessibility)). Also create labels for any customizable Touch Bar controls that you provide so VoiceOver can describe these controls on the customization screen.

# **Gestures**

People use a subset of the standard gestures to interact with the Touch Bar.

# **Tap**

People tap to activate a control, like a button, or select an item, such as an emoji, a color, or a segment in a segmented control.

# **Touch and hold**

A touch and hold gesture initiates a control’s secondary action. In Mail, for example, tapping the Flag button adds a flag to a message, but touching and holding the button reveals a modal view that lets people change the flag’s color.

# **Horizontal swipe or pan**

People use a horizontal swipe or pan to drag an element, like a slider thumb, or navigate through content, such as a list of dates or a group of photos in a scrubber.

# **Multi-Touch**

Although the Touch Bar supports Multi-Touch gestures — like a pinch — such gestures can be cumbersome for people to perform. In general, it’s best to use Multi-Touch gestures sparingly.

# **Best practices**

Keep the following guidance in mind as you design your app’s Touch Bar interfaces.

**Make the Touch Bar relevant to the current context on the main screen.**Identify the different contexts within your app. Then, consider how you can expose varying levels of functionality based on how your app is used.

**Use the Touch Bar as an extension of the keyboard and trackpad, not as a display.** Although the Touch Bar is a screen, its primary function is to serve as an input device — not a secondary display. People may glance at the Touch Bar to locate or use a control, but their primary focus is the main screen. The Touch Bar shouldn’t display alerts, messages, scrolling content, static content, or anything else that distracts people from the main screen.

**Strive to match the look of the physical keyboard.** When possible, aim to design Touch Bar controls that resemble the size and color of keys in the physical keyboard.

**Avoid making functionality available only in the Touch Bar.** Not all devices have a Touch Bar, and people can disable app controls in the Touch Bar if they choose. Always give people ways to perform tasks using the keyboard or trackpad.

**In a full-screen context, consider displaying relevant controls in the Touch Bar.** In full-screen mode, apps often hide onscreen controls and reveal them only when people call for them by, for example, moving the pointer to the top of the screen. If you support full screen, you can use the Touch Bar to give people persistent access to important controls without distracting them from the full-screen experience.

**Prefer controls that produce immediate results.** Ideally, Touch Bar controls give people quick ways to perform actions that would otherwise require extra time spent clicking controls or choosing from menus. Minimize Touch Bar controls that present additional choices, such as popovers. For guidance, see [Controls and views](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar#controls-and-views).

**Be responsive to Touch Bar interactions.** Even when your app is busy doing work or updating the main screen, respond instantly when people use a Touch Bar control.

**When possible, people should be able to start and finish a task in the Touch Bar.** Avoid making people switch to the keyboard or trackpad to complete a task unless the task requires more complex interface controls than the Touch Bar provides.

**Avoid using the Touch Bar for tasks associated with well-known keyboard shortcuts.** The Touch Bar shouldn’t include controls for tasks such as find, select all, deselect, copy, cut, paste, undo, redo, new, save, close, print, and quit. It also shouldn’t include controls that replicate key-based navigation, such as page up and page down.

**Accurately reflect the state of a control that appears in both the Touch Bar and on the main screen.** For example, if a button is unavailable on the main screen, it shouldn't be available in the Touch Bar.

**When responding to user interactions, avoid showing the same UI in both the Touch Bar and the main screen.** For example, when people click the onscreen Emoji & Symbols button in a new message window in Mail, they expect the Character Viewer to open on the main screen, not in the Touch Bar. Unless people interact with the same control in both places, avoid distracting people by displaying redundant UI.

# **Animation**

**Avoid animation.** The Touch Bar is an extension of the keyboard, and people don’t expect animation in their keyboard. In addition, excessive or gratuitous animation can distract people from their work.

# **Color**

**Prefer standard controls and system icons.** The standard controls and system icons already use colors that work well in the Touch Bar. For a list of available system icons, see [Interface icons](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar#interface-icons).

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/TB_visualDesign_colorOne_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/TB_visualDesign_colorOne_2x.png)

**Use color tastefully and minimally.** In general, make the Touch Bar similar in appearance to the physical keyboard. Monochromatic colors work best. If you must use colors in your controls, do so tastefully and primarily in temporary states. Colors shouldn’t appear overwhelming or out of place.

**Use color to denote prominence.** Color can draw the eye to important controls. Reserve blue for default controls and red for destructive controls.

**If you use color, choose a limited palette that coordinates with your app.** Subtle use of color is one way to communicate your brand.

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/TB_visualDesign_colorTwo_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/TB_visualDesign_colorTwo_2x.png)

**Provide wide color artwork.** The Touch Bar supports a P3 color space that can produce richer, more saturated colors than sRGB. Use the Display P3 color profile at 16 bits per pixel (per channel) and export your artwork in the PNG format. For guidance, see [Color management](https://developer.apple.com/design/human-interface-guidelines/foundations/color#color-management).

**TIP**On a Mac that features a wide color display, you can use the system color picker to select and preview P3 colors, and to compare them with sRGB colors.

### **System colors**

macOS offers a range of standard system colors that respond automatically to system white-point changes based on factors such as ambient light and keyboard backlight level.

| Color | API |
| --- | --- |
| Blue | systemBlueColor |
| Brown | systemBrownColor |
| Gray | systemGrayColor |
| Green | systemGreenColor |
| Orange | systemOrangeColor |
| Pink | systemPinkColor |
| Purple | systemPurpleColor |
| Red | systemRedColor |
| Yellow | systemYellowColor |

**Don't replicate system colors.** System color values may fluctuate from release to release and based on various environmental variables. Instead of trying to create custom colors that match the system colors, just use the system colors.

For developer guidance, see [NSColor](https://developer.apple.com/documentation/appkit/nscolor).

### **Dynamic system colors**

macOS defines a range of system colors that dynamically match the color scheme of standard interface controls such as buttons and labels. The following system colors are ideal for use in the Touch Bar.

| Color | Description | API |
| --- | --- | --- |
| Control Color | The system color for the surface of a control. | controlColor |
| Label Color | The system color for the text of a label. | labelColor |
| Secondary Label Color | The system color for label text of lesser importance than labelColor text, for example, a subheading or additional information. | secondaryLabelColor |
| Tertiary Label Color | The system color for label text of lesser importance than secondaryLabelColor, for example, disabled text. | tertiaryLabelColor |
| Quaternary Label Color | The system color for label text of lesser importance than tertiaryLabelColor, for example, disabled text. | quaternaryLabelColor |

# **Layout**

The width of the Touch Bar display differs depending on the device.

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-total_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-total_2x.png)

Touch Bar (2nd generation)

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-total_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-total_2x.png)

Touch Bar (1st generation)

### **Touch Bar areas**

In its standard configuration, the Touch Bar display consists of either two or three areas, depending on the device. The system enforces a 16pt separation between areas.

The Touch Bar (2nd generation) display contains two areas: the app region and the Control Strip. Although the second generation Touch Bar doesn’t include a system button area, you can display a system button within your app region.

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-regions_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-regions_2x.png)

The Touch Bar (1st generation) display includes three areas: the system button area, the app region, and the Control Strip.

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-regions_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-regions_2x.png)

| Area | Contains | User configurable? |
| --- | --- | --- |
| Control Strip | System-level controls for performing actions, like initiating Siri or adjusting the volume level. | Yes. People can extend the Control Strip to the full width of the Touch Bar, collapse it to the right side of the Touch Bar, reduce it in size, or hide it entirely. By default, the Control Strip appears in its collapsed state and contains four controls. |
| App region | Your app’s controls. | Yes. People can hide this area entirely. When the Control Strip is visible, the app region has a minimum width of 685pt. |
| System button (available on some models) | A contextually relevant button, like Esc, Cancel, or Done. | No. When present, this area's width is 64pt. In Touch Bar (2nd generation), you can use 8pt spacing to display the relevant button in the app region, where it's disabled by default. |

**Assume that the default Control Strip is visible.** Although people can reconfigure the Control Strip, reduce its size, or hide it completely, don’t rely on the availability of this space for your design.

### **Positioning app controls**

You have several options for adding visual separation between app controls in the Touch Bar.

| Spacing type | Width between controls |
| --- | --- |
| Default | 8pt |
| Small fixed space | 16pt |
| Large fixed space | 32pt |
| Flexible space | Varies to match the available space. |

**Position controls logically and intuitively.** If your app offers a control that persists across different modalities, it can work well to put the control in the left side of the app region. For example, the Compose button in Notes always appears in the far left of the Touch Bar, regardless of whether people are navigating notes, editing a note, or browsing attachments.

On the other hand, primary controls that command people’s attention — such as an alert or the suggested items in the QuickType bar — work best centered in the app region, with secondary options on the left. Consider using the order of controls in your app’s toolbar to inform the order of Touch Bar controls in the app region. When you use consistent control positions in both areas, people can rely on their familiarity with your onscreen controls to help them use your Touch Bar controls.

**IMPORTANT**If the order of your Touch Bar controls mirrors the order of controls in your app’s window, make sure to adjust the control order in the app region when your app uses a right-to-left layout.

**Construct a flexible layout.** The app region varies in width depending on the configuration of the Control Strip and the device, so consider allowing certain controls — such as sliders and scrubbers — to stretch when additional space becomes available.

**Strive for consistent spacing.** As much as possible, make controls in the Touch Bar equidistant, except when spacing variations are necessary for clarity or to cluster related controls.

**Use flexible spaces and grouping to aid alignment.** Flexible space between items pushes the items on the left toward the left side of the Touch Bar and the items on the right toward the right side of the Touch Bar. Grouping lets you position multiple controls at once. For example, you can center a control or group by marking it as the principal item in the Touch Bar.

**Avoid repositioning controls automatically.** People can become frustrated and confused if a control changes position by itself. If it makes sense in your app, consider letting people customize control positioning.

**Avoid manually reversing controls in right-to-left locales.** The system already reverses certain controls, such as segmented controls and sliders. Manually reversing controls can cause problems with Touch Bar customization features.

For developer guidance, see [NSTouchBarItem](https://developer.apple.com/documentation/appkit/nstouchbaritem).

### **Common layout styles**

Touch Bar layouts can vary significantly from app to app because of factors like configuration options, various control sizes, and the device your app is running on. When possible, use one of the following common layout styles for your controls.

**Layout with one principal item.** The center of the Touch Bar contains a single large control, such as a [candidate list](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar#candidate-lists). Additional controls, such as buttons and segmented controls, are on the left. In Touch Bar (2nd generation), layouts with one principal item can look like this:

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-1principal1_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-1principal1_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-1principal2_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-1principal2_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-1principal3_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-1principal3_2x.png)

**NOTE**In Touch Bar (2nd generation), a principal candidate list control typically remains centered with respect to the device, whereas other types of principal controls may appear off-center in some circumstances. For example, an item might be too large to center in the current configuration, but may become centered when people customize the Control Strip.

In Touch Bar (1st generation), layouts with one principal item can look like this:

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-1principal1_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-1principal1_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-1principal2_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-1principal2_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-1principal3_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-1principal3_2x.png)

**Layout with two principal items.** The center of the Touch Bar contains two consistently sized controls. Additional controls are on the left.

In Touch Bar (2nd generation), a layout with two principal items can look like this:

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-2principal_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-2principal_2x.png)

In Touch Bar (1st generation), a layout with two principal items can look like this:

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-2principal_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-2principal_2x.png)

**Layout with three principal items.** The center of the Touch Bar contains three consistently sized controls. Additional controls are on the left.

In Touch Bar (2nd generation), a layout with three principal items can look like this:

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-3principal_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-3principal_2x.png)

In Touch Bar (1st generation), a layout with three principal items can look like this:

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-3principal_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-3principal_2x.png)

**Fluid layout.** This layout includes consistently-sized controls, such as buttons.

In Touch Bar (2nd generation), a fluid layout can look like this:

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-fluid_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-b-layout-fluid_2x.png)

In Touch Bar (1st generation), a fluid layout can look like this:

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-fluid_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-layout-fluid_2x.png)

# **Typography**

The Touch Bar uses a variant of San Francisco, the system font in macOS. Standard Touch Bar controls, such as buttons and segmented controls, automatically use this variant. For guidance, see [Typography](https://developer.apple.com/design/human-interface-guidelines/foundations/typography); for developer guidance, see [NSFont](https://developer.apple.com/documentation/appkit/nsfont).

# **Interface icons**

macOS provides many interface icons you can use to represent common tasks and types of content in your app’s Touch Bar controls.

When you use AppKit API to display a system-provided glyph, you automatically get an image in the format that’s appropriate for the version of macOS in which your app is running. For example, if your app runs in macOS 11 and later, you get an [SF Symbol](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols/); if your app runs in Catalina or earlier, AppKit continues to provide the existing template image. For developer guidance, see [NSTouchBarItem](https://developer.apple.com/documentation/appkit/nstouchbaritem).

**IMPORTANT**By default, the system APIs return SF symbols configured as 13 pt, large scale, and medium weight.In some cases, a symbol might not have the same size or alignment as the image it replaces, so it’s important to check your layout.

**Prefer system images because people are familiar with them.** Also, system-provided glyphs automatically receive appropriate coloring, respond to system white-point changes based on factors such as ambient light and keyboard backlight level, and respond to user interactions.

**Use each system-defined glyph according to its meaning — not its appearance.** When you choose an image for its meaning, your app can remain visually consistent with the system even if the appearance of the image changes.

**Use only system images that are designed for the Touch Bar.** Don’t use other types of images in the Touch Bar, such as toolbar glyphs.

**Design a custom symbol or image if you can’t find a system-defined one that meets your needs.** Designing a custom symbol or image lets you communicate unique details that help people use your app; repurposing a system-defined image can cause confusion. For guidance, see [Custom Touch Bar icons](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar#custom-touch-bar-icons); for general design guidance, see [Icons](https://developer.apple.com/design/human-interface-guidelines/foundations/icons/).

**NOTE**Some system icons, like Go Back and Go Forward, automatically reverse direction in right-to-left locales.

[제목 없음](https://www.notion.so/e1afda82c9da492c8a5bf4520deb1955)

# **Custom Touch Bar icons**

If your app includes tasks or modes that can’t be represented by a system-provided Touch Bar image, you can create your own. [Apple Design Resources](https://developer.apple.com/design/resources/#macos-apps)provides downloadable Photoshop and Sketch templates you can use to design properly scaled icons for the Touch Bar. For guidance, see [Icons](https://developer.apple.com/design/human-interface-guidelines/foundations/icons).

In general, create icons that look similar to the icons on the physical keyboard keys. Supply high-resolution images with a scale factor of @2x for all artwork that appears in the Touch Bar. To learn about image resolutions, see [Scale factors](https://developer.apple.com/design/human-interface-guidelines/foundations/images#scale-factors).

**Design recognizable icons that clearly relate to your app on the main screen.** If necessary, you can vary the images to match the style of the Touch Bar.

**Avoid icons that extend to the full height of the Touch Bar.** In general, icons shouldn’t exceed 44px in height (36px for circular icons).

|  |  |
| --- | --- |
| Ideal icon size | 18x18 pt (36x36 px @2x) |
| Maximum icon size | 22x22 pt (44x44 px @2x) |

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/TB_custom_icon_example_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/TB_custom_icon_example_2x.png)

**Keep icons optically centered.** Crop artwork to match the icon’s width, then add padding as needed to keep the icon optically centered when it’s displayed in a control.

**Prefer a 45-degree angle for diagonal elements.** Using the same angle as in system icons like [Audio Input Mute](https://developer.apple.com/documentation/appkit/nsimage/2646941-touchbaraudioinputmutetemplatena) and [Compose](https://developer.apple.com/documentation/appkit/nsimage/2544716-touchbarcomposetemplatename) helps your custom icons look at home in the Touch Bar.

**Avoid using color to communicate on and off states.** The system already changes the background appearance of standard controls that are in an off state.

**Give most icons a 100% opacity fill.** To optimize readability, you might want to use a 70% opacity fill in combination with a 100% opacity fill. Use midtones only for improving readability and balance.

For guidance, see [Color](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar#color).

**To match the style of the physical keyboard, give most icons a 2px stroke.** If your design requires more visual weight, consider a 3px stroke.

**As much as possible, match the corner styles of the system images.**For example, use square corners for icons with a 2px stroke, rounded corners with a 1px radius for icons with a 3px stroke, and rounded corners with a 4px radius for solid shapes.

# **Controls and views**

The system offers a range of standard controls you can provide in the app region of the Touch Bar. For consistency, use these controls when possible.

# **Buttons**

Buttons initiate app-specific actions, and can include an icon and a title.

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-buttons_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-buttons_2x.png)

**Prefer icons over titles.** Strive to design clear icons that stand on their own without supporting text.

**Keep titles short.** Lengthy titles can crowd the Touch Bar.

**Customize a button’s bezel color if necessary.** The system-provided button bezel looks similar to the physical keyboard buttons and contributes to a unified visual experience. If your app requires a custom bezel color, consider using a dark color, which tends to look good in the Touch Bar.

For guidance, see [Buttons](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons). For developer guidance, see [NSButton](https://developer.apple.com/documentation/appkit/nsbutton).

### **Toggles**

A toggle switches between on and off states.

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-toggle-on_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-toggle-on_2x.png)

On

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-toggle-off_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-toggle-off_2x.png)

Off

**Let the background indicate a toggle’s state.** The system automatically changes the background appearance of buttons in an off state, so there’s no need to indicate the state using color, text, or a different icon.

**Use toggles in place of checkboxes and radio buttons.** If you need a control that lets people choose between two states, use a toggle button.

For developer guidance, see the [state](https://developer.apple.com/documentation/appkit/nsbutton/1528907-state) property of [NSButton](https://developer.apple.com/documentation/appkit/nsbutton).

# **Candidate lists**

A candidate list offers autocompletion suggestions during text entry. People can tap a suggestion to accept and insert it into the active text field or text view on the main screen. People can also expand or collapse a candidate list. An expanded candidate list replaces other controls that reside within the expansion area.

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-candidate-list_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-candidate-list_2x.png)

For developer guidance, see [NSCandidateListTouchBarItem](https://developer.apple.com/documentation/appkit/nscandidatelisttouchbaritem).

# **Character pickers**

A character picker opens a popover that includes a list of special characters, such as emoji. People can tap a character in the picker to insert it into the active text area on the main screen.

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-character-picker-collapsed_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-character-picker-collapsed_2x.png)

Closed

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-character-picker-expanded_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-character-picker-expanded_2x.png)

Open

For developer guidance, see [NSCandidateListTouchBarItem](https://developer.apple.com/documentation/appkit/nscandidatelisttouchbaritem).

# **Color pickers**

A color picker opens a popover that includes controls for selecting a color. You can configure a color picker to display an icon for a color picker, a stroke color picker, or a text color picker. Regardless of the icon, all color pickers display the same popover.

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-color-picker-collapsed_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-color-picker-collapsed_2x.png)

Closed

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-color-picker-expanded_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-color-picker-expanded_2x.png)

Open

**Use icons as intended.** Use the stroke color picker icon for selecting a stroke color. Use the text color picker icon for selecting a text color. For other color selection scenarios, use the color picker icon.

For developer guidance, see [NSColorPickerTouchBarItem](https://developer.apple.com/documentation/appkit/nscolorpickertouchbaritem).

# **Labels**

A label displays read-only text that doesn’t appear within a control.

**In general, avoid labels.** Although the Touch Bar can display labels, it’s generally best to avoid them because they’re not interactive. Instead, focus on designing meaningful icons for your controls. If you must include a label, keep it as short as possible.

**Prefer titles over labels when supplementing complex icons.** If the meaning of a control’s icon isn’t clear on its own, consider including a short title within the control to provide context.

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-buttons-with-titles_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-buttons-with-titles_2x.png)

For guidance, see [Labels](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/labels). For developer guidance, see [NSTextField](https://developer.apple.com/documentation/appkit/nstextfield).

# **Popovers**

A closed popover looks like a single button in the Touch Bar.

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-popover-closed_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-popover-closed_2x.png)

Closed

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-popover-open_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-popover-open_2x.png)

Open

When it’s open, the popover replaces the current set of controls in the app region with a modal overlay containing a transient set of controls. In this modal overlay, people make a selection or tap a close button to return to the collapsed state and the previous set of controls.

**TIP**In Touch Bar (2nd generation), the popover’s close button appears within the app region; in Touch Bar (1st generation), the close button replaces the system button. The second generation Touch Bar decreases the space available for popovers by 64 points and the system may display controls closer together to avoid clipping controls.

Collapsed popovers open when people tap them. Optionally, popovers can also open in response to a touch and hold gesture. Popovers that support touch and hold include a trailing carat decoration.

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-collapsed-popover-closed_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-collapsed-popover-closed_2x.png)

Closed

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-collapsed-popover-open_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-collapsed-popover-open_2x.png)

Open

A popover can present the same overlay regardless of the gesture people use to expand it, or it can present a different overlay for each gesture. In a touch and hold overlay, people make a selection by sliding their holding finger to a control, and collapse the popover by lifting their finger.

**Use popovers sparingly.** Most controls in the Touch Bar should perform an action with a single tap.

**Avoid nesting popovers.** In general, people should rarely need to navigate more than one level in the Touch Bar.

**Reserve touch and hold for simple popovers.** Use touch and hold primarily to display an overlay that includes a simple set of options — such as a single segmented control — from which people can make a selection.

**Indicate choice selection in a collapsed popover.** When an expanded popover includes a list of options, the collapsed state should show the currently selected option.

**Provide an obvious exit path.** Make sure people always know how to collapse a popover and return to the previous set of controls.

For developer guidance, see [NSPopoverTouchBarItem](https://developer.apple.com/documentation/appkit/nspopovertouchbaritem).

# **Scrubbers**

A scrubber lets people swipe left and right to navigate through content like a list of dates or a group of photos. Scrubbers can be fixed or free, and are highly customizable — but should retain an appearance that doesn’t feel out of place in the Touch Bar.

For developer guidance, see [NSScrubber](https://developer.apple.com/documentation/appkit/nsscrubber).

### **Fixed scrubbers**

A fixed scrubber allows for fluid, continuous interaction with a set of arranged content, such as open Safari tabs. As people swipe across the scrubber, items beneath their finger become highlighted. Depending on the scrubber’s configuration, people make a selection by moving a finger to the item, or by lifting their finger from the scrubber. If the amount of content exceeds the size of a fixed scrubber, the scrubber automatically scrolls to reveal additional items as the finger nears the edge of the control. In a fixed scrubber, people use a finger to move the selection, rather than the content.

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-fixed-scrubber_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-fixed-scrubber_2x.png)

### **Free scrubbers**

A free scrubber presents content in a scrollable list — such as a list of Calendar dates — that people swipe to scroll. Depending on the scrubber’s configuration, people select an item by moving it to a specific location, like the center of the scrubber, or by tapping the item while the scrubber is stationary.

**Use predictable and logically ordered values.** When the scrollable list in a free scrubber is stationary, some values may be hidden. If the list displays items in a logical order that follows an obvious progression, people can predict the hidden values and move through the list quickly. When viewing a list of country or region names, for example, people are generally better at predicting hidden values in an alphabetized list than in a list ordered by population size.

**Keep lists of values as short as possible.** People can find it tedious to navigate long lists in the Touch Bar. If you have a large list of values, consider presenting it on the main screen instead of the Touch Bar, so people can use the keyboard or trackpad for navigation.

# **Segmented controls**

A segmented control is a linear set of two or more segments, each of which functions as a button — usually configured as a toggle. Within the control, all segments are equal in width. Like buttons, segments can contain text and icons.

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-segmented-controls_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-segmented-controls_2x.png)

**Limit the number of segments to improve usability.** Wider segments are easier for people to tap.

**Prefer icons over titles.** Strive to design clear icons that stand on their own without requiring supporting text.

**Try to keep segment content size consistent.** Because segments match in width, it’s visually coherent if the content in the segments is also equal in length.

**Keep titles short.** Lengthy titles can crowd the Touch Bar.

**Prefer darker colors for bezel color changes.** The appearance of the system-provided bezel resembles physical keyboard buttons. If your app requires a custom bezel color, dark colors are recommended.

For developer guidance, see [NSSegmentedControl](https://developer.apple.com/documentation/appkit/nssegmentedcontrol).

# **Sharing service pickers**

People use sharing service pickers to share text, images, and other content with apps, social media accounts, and other services. When people tap a sharing service picker, it displays a popover that contains sharing buttons.

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-sharing-picker-closed_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-sharing-picker-closed_2x.png)

Closed

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-sharing-picker-open_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-sharing-picker-open_2x.png)

Open

**Enable a sharing service picker only when there’s content to share.** If people haven’t selected text, images, or other sharable content, the sharing service picker should be disabled.

For developer guidance, see [NSSharingServicePicker](https://developer.apple.com/documentation/appkit/nssharingservicepicker).

# **Sliders**

A slider is a horizontal track with a control called a thumb, which people can slide to move between a minimum and maximum value, such as screen brightness level, or position during media playback. As a slider’s value changes, the portion of track between the minimum value and the thumb fills with color.

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-slider_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-slider_2x.png)

**Customize a slider’s appearance to match your app and add value.**Consider coordinating a slider’s track color with your app’s color scheme.

**Consider using a stepper instead of a slider when space is tight.** If a slider’s values cover a limited range and it’s possible to move through them in discrete steps, it might make sense to use a stepper. For guidance, see [Steppers](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar#steppers).

**Provide left and right icons that illustrate the meaning of the minimum and maximum values.** A slider that adjusts image size, for example, could show a small image icon on the left and a large image icon on the right.

For developer guidance, see [NSSlider](https://developer.apple.com/documentation/appkit/nsslider).

# **Steppers**

Steppers provide a set of continuous — usually numeric — values from which people can choose. A stepper displays the current value centered between a decrementing control and an incrementing control. People tap the controls or swipe the current value left or right to change the value by an amount you specify.

![https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-steppers_2x.png](https://developer.apple.com/design/human-interface-guidelines/inputs/touch-bar/images/tb-cv-steppers_2x.png)

**Display the item’s current value in the center view.** By default, a stepper uses text to display the current value. You can use a formatter to style the text — for example, in a stepper that lets people choose dates, you might make today’s date red. In some cases, it might make sense to use images instead of text, but it can be tricky to create images that convey a logical progression from which people can predict the values that precede and follow the current value. For example, a stepper that controls the line weight of a marking tool could use a set of images that vary in thickness to help people understand the effect of incrementing and decrementing the value.

**Avoid using a stepper when people are likely to make large adjustments to an item’s value.** Because a stepper changes an item’s value by one discrete step per swipe or tap, people would have to swipe or tap a lot to make a large value change.

# **Platform considerations**

*Not supported in iOS, iPadOS, tvOS, or watchOS.*