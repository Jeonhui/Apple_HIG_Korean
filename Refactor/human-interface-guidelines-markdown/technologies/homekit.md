HomeKit
=======

HomeKit lets people securely control connected accessories in their homes using Siri or the Home app on iPhone, iPad, Apple Watch, and Mac.![A sketch of the HomeKit icon. The image is overlaid with rectangular and circular grid lines and is tinted blue to subtly reflect the blue in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/ebafbd857c1881bf0f090c3592d8a2d6/technologies-HomeKit-intro@2x.png)

In iOS, the Home app also lets people manage and configure accessories.

Your iOS, tvOS, or watchOS app can integrate with HomeKit (and by extension the Home app) to provide a custom or accessory-specific experience. For example, you can:

* Help people set up, name, and organize their accessories
* Allow fine-grained accessory configuration and control
* Provide access to custom accessory features
* Show people how to create powerful, hands-free automations
* Provide support

For developer guidance, see [HomeKit](/documentation/homekit)
. If you’re an MFi licensee, visit the [MFi portal](https://mfi.apple.com)
 for guidance on naming and messaging for accessory packaging.

[Terminology and layout](/design/human-interface-guidelines/homekit#Terminology-and-layout)
-------------------------------------------------------------------------------------------

HomeKit models the home as a hierarchy of objects and defines a vocabulary of terms that refer to them. The Home app uses the HomeKit object model and terminology to give people intuitive control of accessories by voice, app, and automation.

It’s crucial for your app to use the terminology and object model that HomeKit defines, so that you can reinforce people’s understanding and make home automation feel approachable.

In the HomeKit model, the [home](/design/human-interface-guidelines/homekit#Homes)
 object is the root of a hierarchy that contains all other objects, such as [rooms](/design/human-interface-guidelines/homekit#Rooms)
, [accessories](/design/human-interface-guidelines/homekit#Accessories-services-and-characteristics)
, and [zones](/design/human-interface-guidelines/homekit#Zones)
. When there’s more than one home, each home is the root of a different hierarchy.

**Acknowledge the hierarchical model that HomeKit uses.** Even if your app doesn’t organize accessories by rooms and zones in its UI, it’s useful to reference the HomeKit model when helping people set up or control their accessories. People need to know where accessories are located so they can use Siri and HomePod to control them by speaking commands like “Siri, turn on the lights upstairs,” or “It’s dark in here.” For more guidance, see [Siri interactions](/design/human-interface-guidelines/homekit#Siri-interactions)
.

**Make it easy for people to find an accessory’s related HomeKit details.** If your app’s organization focuses on accessories, don’t hide other HomeKit information, such as an accessory’s zone or room, in a hard-to-discover settings screen. Instead, consider making the related HomeKit information easily available in an accessory detail view.

**Recognize that people can have more than one home.** Even if your app doesn’t support the concept of multiple homes per user, consider providing the relevant home information in an accessory detail view.

**Don’t present duplicate home settings.** If your app has a different perspective on the organization of a home, don’t confuse people by asking them to set up all or parts of their homes again or by showing a duplicate settings view. Always defer to the settings people made in the Home app and find an intuitive way to present these details in your UI.

### [Homes](/design/human-interface-guidelines/homekit#Homes)

HomeKit uses the term *home* to represent a physical home, office, or other location of relevance to people. One person might have multiple homes.

### [Rooms](/design/human-interface-guidelines/homekit#Rooms)

A *room* represents a physical room in a home. Rooms don’t have attributes like size or location; they’re simply names that have meaning to people, such as *Bedroom* or *Office*. When people assign accessories to a room, they can use voice commands like “Siri, turn on all the lights except the bedroom,” or “Siri, turn on the kitchen and hallway lights.”

### [Accessories, services, and characteristics](/design/human-interface-guidelines/homekit#Accessories-services-and-characteristics)

The term *accessory* represents a physical, connected home accessory, like a ceiling fan, lamp, lock, or camera. HomeKit uses *category* to represent a type of accessory, such as thermostat, fan, or light. Typically, an accessory manufacturer assigns each accessory to a category, but your app can help people make this assignment if necessary. For example, a switch that’s connected to a fan or a lamp needs to be assigned to the same category as the accessory it controls.

A controllable feature of an accessory, such as the switch on a connected light, is known as a *service*. Some accessories offer multiple services. For example, a connected garage door might let people control the light and the door separately, or a connected outlet might support separate control of the top outlet and the bottom outlet. Apps don’t use the word *service* in the UI; instead, they use names that describe the service, such as *garage door opener* and *ceiling fan light*. When people use Siri to control the accessories in their homes, they speak the service name, not the accessory name. For more guidance on naming, see [Help people choose useful names](/design/human-interface-guidelines/homekit#Help-people-choose-useful-names)
.

A *characteristic* is a controllable attribute of a service. For example, in a ceiling fan, the fan service might have a speed characteristic and the light service might have a brightness characteristic. Apps don’t use the word *characteristic* in the UI; instead, they use terms that describe the attribute, such as *speed* and *brightness*.

A *service group* represents a group of accessory services that someone might want to control as a unit. For example, if there’s a floor lamp and two table lamps in one corner of a room, people might assign all three services to a service group named *reading lamps*. Doing so would let people use the *reading lamps* service group to control these three lights independently of all other lights in the room.

### [Actions and scenes](/design/human-interface-guidelines/homekit#Actions-and-scenes)

The term *action* refers to the changing of a service’s characteristic, such as adjusting the speed of a fan or the brightness of a light. People and automation can initiate actions.

A *scene* is a group of actions that control one or more services in one or more accessories. For example, people might create a *Movie Time* scene that lowers the shades and dims the lights in the living room, or a *Good Morning* scene that turns on the lights, raises the shades, and starts the coffee maker in the kitchen.

Tip

The HomeKit API uses the term *action set* instead of *scene*. In your app’s UI, always use the term *scene*.

### [Automations](/design/human-interface-guidelines/homekit#Automations)

*Automations* cause accessories to react to certain situations, such as when a person’s location changes, a particular time of day occurs, another accessory turns on or off, or a sensor detects something. For example, an automation could turn on the house lights at sunset or when people arrive home.

### [Zones](/design/human-interface-guidelines/homekit#Zones)

A *zone* represents an area in the home that contains multiple rooms, such as *upstairs* or *downstairs*. Setting up a zone is optional, but doing so lets people control multiple accessories at one time. For example, assigning all downstairs lights to a zone named *downstairs* lets people use voice commands like “Siri, turn off all the lights downstairs.”

[Setup](/design/human-interface-guidelines/homekit#Setup)
---------------------------------------------------------

**Use the system-provided setup flow to give people a familiar experience.** The HomeKit setup flow works more quickly than traditional setup flows because it lets people name accessories, join networks, pair with HomeKit, assign room and service categories, and designate favorites in just a few steps. Using the system-provided setup flow also lets your app focus on promoting the custom functionality that makes your accessory unique. For developer guidance, see [`addAndSetupAccessories(with:completionHandler:)`](/documentation/homekit/hmhome/2941039-addandsetupaccessories)
.

**Provide context to explain why you need access to people’s Home data.** Create a purpose string with a phrase that describes why you’re asking for permission to access data, such as “Lets you control this accessory with the Apple Home app and Siri across your Apple devices.”

**Don’t require people to create an account or supply personal information.** Instead, defer to HomeKit for any information you might need. If your app provides additional services that require an account, such as cloud services, make account setup optional and wait until after initial HomeKit setup to offer it.

**Honor people’s setup choices.** When people choose to use HomeKit to set up your accessory, don’t force them to set up other platforms during the HomeKit setup flow. A cross-platform setup experience prevents people from using the accessory right away and can cause confusion by presenting too many ways to control the accessory.

**Carefully consider how and when to provide a custom accessory setup experience.** Always begin by presenting the system-provided setup flow. Then, after the accessory’s basic functionality is available, offer a custom post-setup experience that highlights the unique features of your accessory and helps people get the most out of it. For example, a light manufacturer’s app could help people create personalized light scenes in their homes using key colors scanned in from photos in their library.

### [Help people choose useful names](/design/human-interface-guidelines/homekit#Help-people-choose-useful-names)

**Suggest service names that suit your accessory.** If your app detects when someone creates a suboptimal name for Siri voice controls, recommend alternatives that you know will work well for most people. Never suggest company names or model numbers for use as service names.

**Check that the names people provide follow HomeKit naming rules.** If your app lets people rename services, make sure that the new names follow the rules. (The system-provided setup flow automatically checks the original names.) If people enter a name that breaks one or more rules, briefly explain the problem and suggest some alternative names that work. Here are the rules:

* Use only alphanumeric, space, and apostrophe characters.
* Start and end with an alphabetic or numeric character.
* Don’t include emojis.



|  | Example service names |
| --- | --- |
| A checkmark in a circle to indicate correct usage. | Reading lamp |
| An X in a circle to indicate incorrect usage. | 📚 lamp |
| A checkmark in a circle to indicate correct usage. | 2nd garage door |
| An X in a circle to indicate incorrect usage. | #2 garage door |

**Help people avoid creating names that include location information.** Although it’s natural for someone to use “kitchen light” to name a light in the kitchen, including the room name in the service name can lead to unpredictable results when controlling the accessory by voice. Your app can detect service names that duplicate location information and help people fix them. For example, you might present a post-setup experience that removes the room or zone from a service name and encourages people to assign the accessory to that room or zone instead.

[Siri interactions](/design/human-interface-guidelines/homekit#Siri-interactions)
---------------------------------------------------------------------------------

HomeKit supports powerful, hands-free control using voice commands. You can help people use Siri to interact with accessories, services, and zones in their home quickly and efficiently.

**Present example voice commands to demonstrate using Siri to control accessories during setup.** As soon as people complete the setup of a new accessory, consider using the service name they chose in a few example Siri phrases and encourage people to try them out.

**After setup, consider teaching people about more complex Siri commands.** People might not be aware of the broad range of natural language phrases they can use with Siri and HomePod to control their accessories. After setup is complete, find useful places throughout your app to help people learn about these types of commands. For example, in a scene detail view, you could tell people, *You can say “Hey Siri, set ‘Movie Time.’”*

In addition to recognizing the names of homes, rooms, zones, services, and scenes, Siri can also use information such as accessory category and characteristic to identify a service. For example, when people use terms like *brighter* or *dim*, Siri recognizes that they’re referring to a service that has a brightness characteristic, even if they don’t speak the name of the service.

To illustrate the power and flexibility of Siri commands, here are some examples of the types of phrases that people could use to control their accessories.



| Phrase | Siri understands |
| --- | --- |
| “Turn on the floor lamp” | Service (*floor lamp*) |
| “Show me the entryway camera” | Service (*entryway camera*) |
| “Turn on the light” | Accessory category (*light*) |
| “Turn off the living room light” | Room (*living room*) |
| Accessory category (*light*) |
| “Make the living room a little bit brighter” | Room (*living room*) |
| Accessory category (implied) |
| Brightness characteristic (*brighter*) |
| “Turn on the recessed lights” | Service group (*recessed lights*) |
| “Turn off the lights upstairs” | Accessory category (*lights*) |
| Zone (*upstairs*) |
| “Dim the lights in the bedroom and nursery” | Accessory category (*lights*) |
| Brightness characteristic (*dim*) |
| Rooms (*bedroom*, *nursery*) |
| “Run Good night” | Scene (*Good night*) |
| “Is someone in the living room?” | Accessory category (implied) |
| Occupancy detection characteristic (implied) |
| “Is my security system tripped?” | Accessory category (*security system*) |
| “Did I leave the garage door open?” | Accessory category (*garage door*) |
| Open characteristic (*open*) |
| “Did I forget to turn off the lights in the Tahoe House?” | Accessory category (*lights*) |
| Home (*Tahoe House*) |
| “It’s dark in here” | Current home (*here*) |
| Current room (via HomePod) |
| Accessory category (implied) |

**Recommend that people create zones and service groups, if they make sense for your accessory.** If people might benefit from using context-specific voice commands to control your accessory, suggest these types of interactions and help people set them up. For example, if you provide an accessory such as a light, switch, or thermostat, you could suggest setting up a zone named “upstairs” or a service group named “media center” to support commands like “Siri, turn off the upstairs lights,” or “Siri, activate the media center.”

**Offer shortcuts only for accessory-specific functionality that HomeKit doesn’t support.** HomeKit lets people use ordinary (or natural) language to control accessories without requiring any additional configuration, so you avoid confusing people by offering shortcuts that duplicate HomeKit functionality. Instead, consider offering shortcuts for complementary functionality that your app provides. For example, if people often want to order filters for an air conditioner that you support, you might offer a shortcut like “Order AC filters.” To learn how to provide phrases that people can use for shortcuts, see [Shortcuts and suggestions](/design/human-interface-guidelines/siri#Shortcuts-and-suggestions)
.

**If your app supports both HomeKit and shortcuts, help people understand the difference between these types of voice control.** People can get confused if they’re presented with multiple methods of voice control. Be sure you clearly indicate what’s possible with shortcuts, and never encourage people to create a shortcut for a scene or action that HomeKit already supports.

[Custom functionality](/design/human-interface-guidelines/homekit#Custom-functionality)
---------------------------------------------------------------------------------------

Your app is a great place to help people appreciate the unique functionality of your accessory. For example, an app for a light that displays different colors could help people create HomeKit scenes using colors imported from their photos.

**Be clear about what people can do in your app and when they might want to use the Home app.** For example, if your app supports only lights, consider encouraging people to create a “Movie Time” scene that not only dims the lights, but also closes the shades, and turns on the TV to a specific input. To do this, first guide people to set up a scene that includes only your accessory’s actions — in this scenario, dimming the lights. Then, your app can suggest that people open the Home app to add their HomeKit-compatible shades and TV to the scene you helped them create. For guidance on how to refer to the Home app, see [Referring to HomeKit](/design/human-interface-guidelines/homekit#Referring-to-HomeKit)
.

**Defer to HomeKit if your database differs from the HomeKit database.** Give people a seamless experience by automatically reflecting changes made in the Home app or in other third-party HomeKit apps. If you must ask people to manage conflicts in your app, present the conflict visually so that they have a clear picture of the choice they need to confirm. For example, if someone changes an accessory’s service name in the Home app, your app can detect this change and could show both names side by side to confirm that the person wants to use the new name in your app, too.

**Ask permission to update the HomeKit database when people make changes in your app.** You don’t want to surprise people by changing something in the Home app, so it’s essential to get permission or an indication of intent before you write to the database. In particular, never overwrite HomeKit database settings without a person’s explicit direction.

### [Cameras](/design/human-interface-guidelines/homekit#Cameras)

Your app can display still images or streaming video from a connected HomeKit IP camera.

**Don’t block camera images.** It’s fine to supplement the camera’s content with useful features, such as an alert calling attention to potentially interesting activity. However, avoid covering portions of the camera’s images with other content.

**Show a microphone button only if the camera supports bidirectional audio.** A nonfunctioning microphone button takes up valuable display space in your app and risks confusing people.

[Using HomeKit icons](/design/human-interface-guidelines/homekit#Using-HomeKit-icons)
-------------------------------------------------------------------------------------

Use the HomeKit icon in setup or instructional communications related to HomeKit technology.

![The HomeKit icon.](https://docs-assets.developer.apple.com/published/e1fff743af283f526d9b66d5f94fcd23/homekit-glyph@2x.png)

In addition, you can use the Apple Home app icon when referencing the Apple Home app or in a button that opens the Apple Home app [product page](https://itunes.apple.com/us/app/home/id1110145103?mt=8)
 in the App Store.

![The Apple Home app icon, which includes a stylized house with a chimney on the right side of its roof, depicted in graduated shades of orange.](https://docs-assets.developer.apple.com/published/01f390ab7d0057a57277f0dd11b88a83/homeapp-icon@2x.png)

**Use only Apple-provided icons.** Don’t create your own HomeKit or Home app icon design or attempt to mimic the Apple-provided designs. Download HomeKit icons in [Resources](https://developer.apple.com/design/resources/)
.

### [Styles](/design/human-interface-guidelines/homekit#Styles)

You have several options for displaying the HomeKit icon.

#### [Black HomeKit icon](/design/human-interface-guidelines/homekit#Black-HomeKit-icon)

Use the HomeKit icon on white or light backgrounds when other technology icons appear in black.

![A black outlined HomeKit icon.](https://docs-assets.developer.apple.com/published/8979d07d70c66a8f8d74c376b9e6dc6c/homekit-black-icon-set@2x.png)

#### [White HomeKit icon](/design/human-interface-guidelines/homekit#White-HomeKit-icon)

Use the HomeKit icon on black or dark backgrounds when other technology icons appear in white.

![A white outlined HomeKit icon.](https://docs-assets.developer.apple.com/published/e37387a28a0b2451333617e03fa49fa7/homekit-white-icon-set@2x.png)

#### [Custom color HomeKit icon](/design/human-interface-guidelines/homekit#Custom-color-HomeKit-icon)

Use a custom color when other technology icons appear in the same color.

![A blue outlined HomeKit icon.](https://docs-assets.developer.apple.com/published/68a736850a52d6e6a002b698165d1cfb/homekit-custom-color-icon-set@2x.png)

**Position the HomeKit icon consistently with other technology icons.** When other technology icons are contained within shapes, treat the HomeKit icon in the same manner.

![An illustration of three app icons listed in a vertical row on a Settings screen on iPhone. Text above the icons reads 'Integrate with'. The leftmost app icon is the HomeKit icon in a circle, above the text 'Apple HomeKit'. The remaining two app icons contain squares with dashed frames witihn circles, above text that reads 'Name'.](https://docs-assets.developer.apple.com/published/ff72e787a20d3acf190cb442bfb1053a/homekit-settings@2x.png)

**Use the HomeKit icon noninteractively.** Don’t use the icon and the name *HomeKit* in custom interactive elements or buttons. You can use the Apple Home app icon to open the app’s product page in the App Store.

![An illustration of an incorrectly used HomeKit icon in a circular button styled with a chrome appearance.](https://docs-assets.developer.apple.com/published/08c6b1888cd04ea864bfe8d037eb1814/homekit-donot1@2x.png)

![An X in a circle to indicate incorrect usage.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout@2x.png)

![An illustration of a button incorrectly titled 'HomeKit' with a custom gradient background.](https://docs-assets.developer.apple.com/published/0c8ae4ebd1f0d755d78391a46602eda0/homekit-donot2@2x.png)

![An X in a circle to indicate incorrect usage.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout@2x.png)

**Don’t use the HomeKit icon within text or as a replacement for the word HomeKit.** See [Referring to HomeKit](/design/human-interface-guidelines/homekit#Referring-to-HomeKit)
 to learn how to properly reference HomeKit in text.

![The first in a series of images showing examples of the HomeKit icon when used in text. In this example, the icon correctly appears first in the line, and then the text 'Lights set with HomeKit.'](https://docs-assets.developer.apple.com/published/bc6adce917d037e9baa34462f78cb753/homekit-lights-right@2x.png)

![A checkmark in a circle to indicate correct usage.](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark@2x.png)

![The second in a series of images showing examples of the HomeKit icon when used in text. This example depicts the icon incorrectly positioned after the word 'with' in the text 'Lights set with HomeKit.'](https://docs-assets.developer.apple.com/published/7b5582f3e9e67fb2fe4b1a17b08120bc/homekit-lights-wrong1@2x.png)

![An X in a circle to indicate incorrect usage.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout@2x.png)

![The third in a series of images showing examples of the HomeKit icon when used in text. This example depicts the icon incorrectly positioned at the end of the line of text that reads 'Lights set with'.](https://docs-assets.developer.apple.com/published/8132b892760df83913893fe377dc4841/homekit-lights-wrong2@2x.png)

![An X in a circle to indicate incorrect usage.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout@2x.png)

**Pair the icon with the name *HomeKit* correctly.** You can show the name below or beside the icon if other technologies are referenced in this way. Use the same font that’s used on the rest of your layout. For related guidance, see [Referring to HomeKit](/design/human-interface-guidelines/homekit#Referring-to-HomeKit)
.

![An illustration of a view containing setup information within an app. The top of the view includes the title 'Setup' above a divider line. Three rows with icons, text, and disclosure buttons for displaying additional information appear below the divider. The first row includes the HomeKit icon followed by the word 'HomeKit'. The other  two rows display dashed squares representing other app icons, each followed by the word 'Name'.](https://docs-assets.developer.apple.com/published/1db6cad3c43519bd380d54193028059a/homekit-setup@2x.png)Using the icon and name in setup or instructional content![An illustration of a view containing a grid of four app buttons. The top of the view includes the title 'Apps' above a divider line. Two rows of buttons and labels appear below the divider. The first button in the first row includes the Apple Home app icon, and appears above the text 'Apple Home'. The remaining buttons include dashed squares representing other app icons, and each appears above the text 'App Name'.](https://docs-assets.developer.apple.com/published/df2f1eafcb3cce3a74f22edb0a5193a4/homekit-apps@2x.png)Using the icon and name referencing the Apple Home app[Referring to HomeKit](/design/human-interface-guidelines/homekit#Referring-to-HomeKit)
---------------------------------------------------------------------------------------

**Emphasize your app over HomeKit.** Make references to HomeKit or Apple Home less prominent than your app name or main identity.

**Adhere to Apple’s trademark guidelines.** Apple trademarks can’t appear in your app name or images. In text, use Apple product names exactly as shown on the [Apple Trademark List](https://www.apple.com/legal/intellectual-property/trademark/appletmlist.html)
.

* Use Apple product names in singular form only; do not make Apple product names possessive.
* Don’t translate Apple, Apple Home, HomeKit, or any other Apple trademark.
* Don’t use category descriptors. For example, say iPad, not tablet.
* Don’t indicate any kind of sponsorship, partnership, or endorsement from Apple.
* Attribute Apple, HomeKit, and all other Apple trademarks with the correct credit lines wherever legal information appears within your app.
* Refer to Apple devices and operating systems only in technical specifications or compatibility descriptions.



|  | Example text |
| --- | --- |
| A checkmark in a circle to indicate correct usage. | Use HomeKit to turn on your lights from your iPhone or iPad. |
| An X in a circle to indicate incorrect usage. | Use HomeKit to turn on your lights from your iOS devices. |

See [Guidelines for Using Apple Trademarks](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html)
.

### [Referencing HomeKit and the Home app](/design/human-interface-guidelines/homekit#Referencing-HomeKit-and-the-Home-app)

**Use correct capitalization when using the term *HomeKit*.** *HomeKit* is one word, with an uppercase *H* and uppercase *K*, followed by lowercase letters. *Apple Home* is two words, with an uppercase *A* and uppercase *H*, followed by lowercase letters. If your layout displays only all-uppercase designations, *HomeKit* or *Apple Home* can be typeset in all uppercase to match the style of the rest of the layout.

**Don’t use the name *HomeKit* as a descriptor.** Instead use terms like *works with*, *use*, *supports*, or *compatible*.



|  | Example text |
| --- | --- |
| A checkmark in a circle to indicate correct usage. | [Brand] lightbulbs work with HomeKit. |
| A checkmark in a circle to indicate correct usage. | HomeKit-enabled thermostat. |
| A checkmark in a circle to indicate correct usage. | You can use HomeKit with [App Name]. |
| An X in a circle to indicate incorrect usage. | HomeKit lightbulbs. |

**Don’t suggest that HomeKit is performing an action or function.**



|  | Example text |
| --- | --- |
| A checkmark in a circle to indicate correct usage. | Back door is unlocked with HomeKit. |
| An X in a circle to indicate incorrect usage. | HomeKit unlocked the back door. |

**Use the name *Apple* with the name *HomeKit*, if desired.**



|  | Example text |
| --- | --- |
| A checkmark in a circle to indicate correct usage. | Compatible with Apple HomeKit. |

**Use the name *HomeKit* for setup, configuration, and instructions, if desired.**



|  | Example text |
| --- | --- |
| A checkmark in a circle to indicate correct usage. | Open HomeKit settings. |

**Use the app name *Apple Home* whenever referring specifically to the app.** On the first mention of the app in body copy, use the complete name *Apple Home*. Subsequent mentions can refer to the Home app.



|  | Example text |
| --- | --- |
| A checkmark in a circle to indicate correct usage. | Open the Apple Home app. |
| A checkmark in a circle to indicate correct usage. | Open the Apple Home app. Your accessory and room will now appear in the Home app. |
| An X in a circle to indicate incorrect usage. | Open Home. |

[Platform considerations](/design/human-interface-guidelines/homekit#Platform-considerations)
---------------------------------------------------------------------------------------------

*No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

[Resources](/design/human-interface-guidelines/homekit#Resources)
-----------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/homekit#Related)

[Apple Design Resources](https://developer.apple.com/design/resources/)


[Guidelines for Using Apple Trademarks and Copyrights](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html)


#### [Developer documentation](/design/human-interface-guidelines/homekit#Developer-documentation)

[HomeKit](/documentation/homekit)


#### [Videos](/design/human-interface-guidelines/homekit#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/119/8C81F0E7-2E4C-4F4F-82FE-A9EBC73A913D/5239_wide_250x141_1x.jpg) Add support for Matter in your smart home app](https://developer.apple.com/videos/play/wwdc2021/10298) 
[Change log](/design/human-interface-guidelines/homekit#Change-log)
-------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| May 2, 2023 | Consolidated guidance into one page. |

