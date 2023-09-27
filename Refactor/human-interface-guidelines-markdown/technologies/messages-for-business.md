Messages for Business
=====================

Messages for Business helps customers connect with businesses through the Messages app in iOS, iPadOS, macOS, visionOS, and watchOS.![A sketch of a conversation bubble containing elements, suggesting a Messages discussion. The image is overlaid with rectangular and circular grid lines and is tinted blue to subtly reflect the blue in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/f9c5716cb8060fb09ff96ad50136f670/technologies-Messages-for-Business-intro@2x.png)

Using the Messages app, people can contact your company to ask questions, get support, schedule appointments, make payments with Apple Pay, and more.

People can use apps, features, and services like Maps and Spotlight to discover businesses and seamlessly initiate conversations with them. The familiar Messages app interface on iPhone, iPad, Mac, and Apple Watch ensures that customer interaction is intuitive and efficient, and the informality of messaging produces a customer service experience that feels personal and meaningful.

For developer guidance, and to sign up, see [Messages for Business Accounts](https://register.apple.com/resources/messages/messaging-documentation/)
.

[Branding](/design/human-interface-guidelines/messages-for-business#Branding)
-----------------------------------------------------------------------------

Although Messages for Business conversations occur within the experience of the Messages app, you can still leverage your logo and color scheme to call attention to your brand and build a memorable conversation experience.

![A screenshot of a Messages for Business conversation on iPhone. In the conversation, the sender asks to purchase flowers. The business responds asking for some details, then provides a link to make a purchase.](https://docs-assets.developer.apple.com/published/09e99fbae55fcb98942bbeda535f8231/business-nav-bar@2x.png)**Strive for uniqueness.** It’s critical to avoid building an experience that might cause people to confuse your brand with other brands. In particular, your logo design and use of color must never cause people to think they’re conversing with Apple.

For related guidance, see [Color](/design/human-interface-guidelines/messages-for-business#Color)
 and [Logo](/design/human-interface-guidelines/messages-for-business#Logo)
.

[Buttons](/design/human-interface-guidelines/messages-for-business#Buttons)
---------------------------------------------------------------------------

Customers use Messages for Business buttons to start a conversation with your company. You can also support system features like Maps and Spotlight, so that customers can use them to locate your business and start a conversation. Other ways to help customers contact you are to:

* Turn on Message Suggest for your account (see [Triggering message suggest](https://register.apple.com/resources/messages/messaging-documentation/message-suggest#triggering-message-suggest)
)
* Include a URL in an email message (see [Starting a message from a URL](https://register.apple.com/resources/messages/messaging-documentation/message-with-customers#starting-a-message-from-a-url)
)
* Add Messages for Business buttons to your app or your company’s website (see [Design your website and app for the Messages buttons](https://register.apple.com/resources/messages/messaging-documentation/message-with-customers#design-your-website-and-app-for-the-messages-buttons)
)

![A screenshot of a search results screen on iPhone, which lists a business as a top hit. The business listing includes buttons to call, navigate to, or message the business. The listing also includes a button to tap for more information about the business.](https://docs-assets.developer.apple.com/published/1d63b6179445751597142eab92bd77d1/starting-conversation-1@2x.png)![A screenshot of a detail screen that includes a logo and business name, and denotes the business is verified. The screen also includes details about the business, including Messages for Business hours, a link to view a website, and a button to message the business.](https://docs-assets.developer.apple.com/published/98c8f99651706343deb16c078797f058/starting-conversation-2@2x.png)**Let people start conversations anytime.** Don’t dim or turn off buttons or links that initiate conversations outside of your business hours. Even if you only respond to customer service inquiries during certain hours, people need to be able to start a conversation anytime. If a customer starts a conversation after hours when live agents aren’t available, an automated agent needs to send a reply letting them know when a live agent is able to respond.

The following guidelines help you use Messages for Business buttons correctly and refer appropriately to the feature in all your customer-facing communications. To learn how to create screenshots that show customers how Messages for Business interactions work with your company, see [Screenshots](/design/human-interface-guidelines/messages-for-business#Screenshots)
.

### [Using Messages for Business buttons](/design/human-interface-guidelines/messages-for-business#Using-Messages-for-Business-buttons)

Use Messages for Business buttons in places where customers might want to contact your business. For example, use the buttons in your app, on your website, or in an email to make it easy for people to start a new conversation.

* [App](#)
* [Website](#)
* [Email](#)
![An illustration that represents an app screen on iPhone. The screen includes a Messages for Business Ask a Question button.](https://docs-assets.developer.apple.com/published/9c6779fdb4fff6e65e4349999dbed857/entry-point-app@2x.png)

![An illustration that represents a webpage on Mac. The webpage includes a Messages for Business Get Help button.](https://docs-assets.developer.apple.com/published/a7e42ba5de9192feefbd8a94cfe0ec49/entry-point-website@2x.png)

![An illustration that represents an app screen on iPhone. The screen includes a Messages for Business Message Us button.](https://docs-assets.developer.apple.com/published/79670226d236d1b5eeb6f9db1cf71878/entry-point-email@2x.png)

**Let the default button title encourage customers to contact you.** System-provided button titles like “Message Us,” “Get Help,” “Ask a Question,” or “Contact an Agent” help people understand what the button does. If you use the logo-only button, consider displaying the text “Apple Messages” near the button to help people recognize the service.

**Show the buttons on supported devices.** If a customer is using an unsupported device, don’t encourage a conversation by displaying a button — on websites, the button hides automatically when it isn’t supported. If the button is hidden, update the layout accordingly and remove the call to action or other related text.

**Make sure Messages for Business buttons are discoverable.** People generally expect to find the button on contact information, support, order confirmation, product, and order history pages.

**Display the button prominently.** Make Messages for Business buttons the same size or larger than similar contact initiation buttons, such as an email button.

**Use only approved button styles.** For guidance, see [Design your website and app to include the Messages buttons](https://register.apple.com/resources/messages/messaging-documentation/message-with-customers#design-your-website-and-app-for-the-messages-buttons)
.

**Maintain minimum and maximum button sizes and inner side margins.** Use the following values for guidance.



| Max width | Min height | Max height | Min side margins |
| --- | --- | --- | --- |
| 1000 pt (2000 px @2x) | 40 pt (80 px @2x) | 150 pt (300 px @2x) | 5% of height |

**Don’t make any other visual or functional modifications to buttons.** For example, don’t change transparency values or add drop shadows.

**Maintain minimum clear space.** The minimum amount of clear space required around the buttons is 10% of the button’s height. Don’t let other elements infringe on this space or occlude the button in any way.

**Maintain the minimum button size and margin values when manually placing buttons on a webpage.** You’re responsible for sizing and placing the buttons correctly.

Use the following margin values for guidance.



| Margin | Minimum value |
| --- | --- |
| Top and bottom | 15 pt (15 px @1x, 30 px @2x) |
| Left and right | 20 pt (20 px @1x, 40 px @2x) |
| Between buttons | 15 pt (15 px @1x, 30 px @2x) |

For developer guidance, see [Starting a message from a URL](https://register.apple.com/resources/messages/messaging-documentation/message-with-customers#starting-a-message-from-a-url)
 and [Adding a Messages button to your website](https://register.apple.com/resources/messages/messaging-documentation/message-with-customers#adding-a-messages-button-to-your-website)
.

### [Referring to Apple Messages for Business](/design/human-interface-guidelines/messages-for-business#Referring-to-Apple-Messages-for-Business)

**In general, use the terms *Apple Messages for Business* or *Apple Messages* in customer-facing communications.** Avoid using the term *Messages* by itself, especially when paired with a logo-only button.

**Use proper capitalization when mentioning *Apple Messages for Business* in headlines and copy.** Specifically, use four words with an uppercase *A*, an uppercase *M*, and an uppercase *B*, and lowercase for all other letters.

**Avoid using other terms to refer to Messages for Business in customer-facing content.** For example, avoid using the terms *chat* or *text* to refer to a Messages for Business button or flow.

**Never use the Apple logo to represent the name *Apple* in text.** Apple Messages for Business is a service mark of Apple Inc.



|  | Example text |
| --- | --- |
| A checkmark in a circle to indicate correct usage. | Apple Messages for Business |
| A checkmark in a circle to indicate correct usage. | Apple Messages |
| An X in a circle to indicate incorrect usage. | Apple messages for business |
| An X in a circle to indicate incorrect usage. | iMessage |
| An X in a circle to indicate incorrect usage. | APPLE MESSAGES FOR BUSINESS |
| An X in a circle to indicate incorrect usage. |  Messages for Business |

#### [Referring to Apple products](/design/human-interface-guidelines/messages-for-business#Referring-to-Apple-products)

**Adhere to [Guidelines for Using Apple Trademarks](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html)
.** Apple trademarks must not appear in your app name or images. In text, use Apple product names exactly as shown in [Apple Trademark List](https://www.apple.com/legal/intellectual-property/trademark/appletmlist.html)
 — never make them plural or possessive.

[Color](/design/human-interface-guidelines/messages-for-business#Color)
-----------------------------------------------------------------------

When configuring your Messages for Business experience, you can customize the colors of the conversation navigation bar and its back and Info buttons in iOS. These same colors appear in the message header in watchOS, brand name in watchOS, and recipient bubble in macOS.

![An illustration of a Messages for Business navigation bar on iPhone, with sufficent color contrast between the background and other elements.](https://docs-assets.developer.apple.com/published/3375fc61f794b858e7fba74e857ec25a/nav-bar-color-contrast-1-top@2x.png)

![A checkmark in a circle to indicate correct usage.](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark@2x.png)

![An illustration of a Messages for Business navigation bar on iPhone, with insufficent color contrast between the background and other elements.](https://docs-assets.developer.apple.com/published/5a952a9270003702b0550ad21f39100f/nav-bar-color-contrast-2-top@2x.png)

![An X in a circle to indicate incorrect usage.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout@2x.png)

**Use sufficient color contrast ratios.** Insufficient contrast makes content hard to see and can cause logos and buttons to blend in with the background. An online color contrast calculator can help you accurately analyze color contrast. Strive for a minimum contrast ratio of 4.5:1, although 7:1 is preferred because it meets more stringent accessibility standards. For guidance, see [Color and effects](/design/human-interface-guidelines/accessibility#Color-and-effects)
.

[Dark Mode](/design/human-interface-guidelines/messages-for-business#Dark-Mode)
-------------------------------------------------------------------------------

On iPhone, your customers can use the system-wide appearance called Dark Mode. Because Dark Mode uses a darker color palette, you might need to redesign your logo and picker icons so that they look good in both light and dark appearances.

* [Wide logo](#)
* [Messages list or square logo](#)
* [List picker](#)
* [Time picker](#)
![A screenshot a Messages for Business conversation on iPhone. A wide logo appears in the navigation bar above the conversation.](https://docs-assets.developer.apple.com/published/f1d5b214cbbde976c8b93e74f7e71e3b/wide-logo-dark-mode@2x.png)![A screenshot of a Messages list screen on iPhone. The first message in the list is a Messages for Business conversation, and includes a square logo.](https://docs-assets.developer.apple.com/published/6a9731f8ffe842cd613b9d9a67bff2a6/messages-list-dark-mode@2x.png)![A screenshot of a Messages for Business list picker screen on iPhone. The screen includes a list of support options for selection.](https://docs-assets.developer.apple.com/published/97efd4ed689bf22f098fa8b040f18a7f/list-picker-dark-mode@2x.png)![A screenshot of a Messages for Business time picker on iPhone. The screen includes a list of dates, each of which offers multiple time options.](https://docs-assets.developer.apple.com/published/6e3c4e115ca7376873391bc7b3b771c8/time-picker-dark-mode@2x.png)**Use colors that contrast well with both light and dark color palettes.** For example, dark transparencies and colors aren’t visible in Dark Mode.

[Logo](/design/human-interface-guidelines/messages-for-business#Logo)
---------------------------------------------------------------------

Your logo visually identifies your business in Messages and other contexts throughout the system.

**Test your logo’s appearance in all contexts.** View your logo in the message list, conversation navigation bar, and notifications, and make sure it’s clear and distinct.

**Provide your logo in both square and wide variations.** Make sure your logo looks great everywhere by creating a separate version for each variation.

**Use adequate padding in your logo.** Unless your logo has full-bleed elements, it’s best to inset key elements from the edges by 10% of the image’s width and height.

![An illustration of a square logo surrounded by a shaded area that represents padding. Callouts denote the padding measures 10 percent of the logo’s height and width.](https://docs-assets.developer.apple.com/published/dcb08cd57615f35f702a4027d9c3670f/business-square-logo@2x.png)

**Avoid using colors that make it hard for people to perceive your logo.** For example, colorblind people might not be able to distinguish some color combinations, and insufficient contrast can cause icons and text to blend with the background and make content hard to read. For guidance, see [Color and effects](/design/human-interface-guidelines/accessibility#Color-and-effects)
.

### [Square logo](/design/human-interface-guidelines/messages-for-business#Square-logo)

Your square logo appears on the contact card for your business, in search results, in the message list view, and in the navigation bar of a conversation if you don’t provide a wide logo.

![A screenshot of a business detail screen on iPhone. The screen includes a square logo and information about the business.](https://docs-assets.developer.apple.com/published/d4be5bc6da1dfbc008d943ac788a1472/logo-place-card@2x.png)

| Attribute | Value |
| --- | --- |
| Background | Full color |
| Color space | sRGB or P3 |
| Format | PNG or JPEG |
| Layers | Flattened |
| Maximum file size | 2 MB |
| Minimum dimensions | 1024x1024 px |
| Padding | 10% of the image’s width and height |
| Resolution | @3x |
| Shape | Square canvas |
| Transparency | No |

### [Wide logo](/design/human-interface-guidelines/messages-for-business#Wide-logo)

Your wide logo appears in the navigation bar of a conversation.

![An illustration a Messages for Business conversation on iPhone. A wide logo appears in the navigation bar above the conversation.](https://docs-assets.developer.apple.com/published/e45bb8b4e2b890215d20f21de55f0360/business-wide-logo@2x.png)



| Attribute | Value |
| --- | --- |
| Background | Transparent |
| Color space | sRGB or P3 |
| Format | PNG |
| Layers | Flattened with transparency as appropriate |
| Maximum file size | 2 MB |
| Maximum width | 1706 px |
| Minimum height | 256 px |
| Resolution | @3x |
| Shape | Rectangular canvas. Allow transparency to define the logo shape. |
| Transparency | Yes |

[Message bubble content](/design/human-interface-guidelines/messages-for-business#Message-bubble-content)
---------------------------------------------------------------------------------------------------------

Message bubbles for standard interactive messages like Apple Pay payment requests, rich links, and pickers include a title, and can optionally include additional text and an image (which can be a video thumbnail). Optional text includes a primary, secondary, and tertiary subtitle, and an image title and subtitle.

### [Message bubble layout styles](/design/human-interface-guidelines/messages-for-business#Message-bubble-layout-styles)

Message bubbles for standard interactive messages support the following layout styles.



| Style | Description | Size |
| --- | --- | --- |
| Icon | Horizontal bubble with an icon | 280x65 pt |
| Small | Horizontal bubble with a small image | 280x85 pt |
| Large | Horizontal bubble with a large image | 280x210 pt |

**Scale images based on the layout style.** When using the same image for multiple layout styles, provide a scaled image variation for each layout style. See [Image sizes](/design/human-interface-guidelines/messages-for-business#Image-sizes)
 for sizing guidance.

### [Images for message bubbles](/design/human-interface-guidelines/messages-for-business#Images-for-message-bubbles)

In a conversation, you can add an image to an interactive message bubble to provide greater context. When asking the customer to choose a product, for example, you could show product photos in a list picker to help people visually distinguish the items. Or, when requesting payment, you could show the item being purchased in the Apple Pay message bubble.

When you include a rich link to a video in a message bubble, you supply a thumbnail image that represents the video. The following size and resolution guidelines apply equally to images and video thumbnails.

#### [Image sizes](/design/human-interface-guidelines/messages-for-business#Image-sizes)

Provide images at the following sizes, based on where the images are used. When displaying the same image at multiple sizes, provide a separate image for each size.



| Usage | Image Size |
| --- | --- |
| Interactive message message bubble (icon) | 40x40 pt (120x120 px @3x) |
| Interactive message message bubble (small) | 60x60 pt (180x180 px @3x) |
| Interactive message message bubble (large) | 263x150 pt (789x450 px @3x) |
| List picker image | 60x60 pt (180x180 px @3x) |

#### [Designing high-resolution images](/design/human-interface-guidelines/messages-for-business#Designing-high-resolution-images)

A standard-resolution display has a 1:1 pixel density (or @1x), where one pixel is equal to one point. High-resolution displays have a higher pixel density, offering a scale factor of 2.0 or 3.0 (referred to as @2x and @3x). As a result, high-resolution displays demand images with more pixels.

![An illustration of an enlarged pixelated circle. The illustration represents standard 1x resolution, and is 10 pixels high by 10 pixels wide.](https://docs-assets.developer.apple.com/published/a9b04545f30aff45ca503e263c02d464/image-resolution-1x@2x.png)1x (10x10 px)![An illustration of an enlarged pixelated circle. The illustration represents high resolution at scale factor of 2x, and is 20 pixels high by 20 pixels wide.](https://docs-assets.developer.apple.com/published/cf203acc0ee6299833fb2e5b5c4a7348/image-resolution-2x@2x.png)2x (20x20 px)![An illustration of an enlarged pixelated circle. The illustration represents high resolution at scale factor of 3x, and is 30 pixels high by 30 pixels wide.](https://docs-assets.developer.apple.com/published/0de9ee5144fc2278682eb211ac8f571d/image-resolution-3x@2x.png)3x (30x30 px)For example, suppose you have a standard resolution (@1x) image that’s 100x100 px. The @2x version of this image would be 200x200 px, and the @3x version would be 300x300 px.

**Always provide high-resolution images with a scale factor of @3x.** The @3x images you provide automatically scale down to @2x or @1x for display at lower resolutions.

**Produce artwork in the appropriate format.** Use de-interlaced PNG files for bitmap/raster artwork. Use JPEG for photos.

**Use the 8-bit color palette for PNG graphics that don’t require full 24-bit color.** Using an 8-bit color palette reduces file size without reducing image quality.

**Optimize JPEG files to find a balance between size and quality.** Most JPEG files can be compressed without noticeable degradation of the resulting image. Even a small amount of compression can save significant disk space. Experiment with compression settings on each image to find the optimal value that yields an acceptable result.

[Screenshots](/design/human-interface-guidelines/messages-for-business#Screenshots)
-----------------------------------------------------------------------------------

By creating screenshots to display on your website or in emails, you can show customers the benefits of using Messages for Business to communicate with your company.

![A screenshot of a Messages for Business conversation on iPhone. The conversation includes a rich link that shows an illustration of a cabinet, the cabinet's price, and a button to purchase the cabinet with Apple Pay.](https://docs-assets.developer.apple.com/published/97acbb5730d0567d671d21d27c135272/rich-link-yes@2x.png)Although you can create custom screenshots from scratch, the easiest method is to download the Messages for Business templates from [Apple Design Resources](https://developer.apple.com/design/resources/#technologies)
 and edit them as needed. These templates include components — such as a message list, conversation view, time picker, and list picker — and symbols. You can also download an iPhone 11 Pro device frame in which to display the screenshots.

Regardless of how you choose to create your screenshots, ensure that they look good and depict conversations accurately. To help make screenshots look realistic, use SF Pro Regular for conversation text (you can download the San Francisco family of fonts [here](https://developer.apple.com/fonts/)
).

### [Status bar](/design/human-interface-guidelines/messages-for-business#Status-bar)

The system-provided status bar appears at the top edge of the screen and displays information like current time, cellular carrier, network connection status, and battery level. The status bar’s background is transparent by default, and the information it displays can be light or dark, depending on the appearance of the content behind it. It’s important to include the status bar in the screenshots you create, because people expect to see it in a messaging experience.

For consistency, use the following values in every status bar you create:

* Time is 9:41. Use SF Pro Regular and don’t add a.m. or p.m.
* Cellular and Wi-Fi icons show maximum connectivity.
* Battery is full and doesn’t include the charging glyph.

![An illustration of a status bar that shows a time of 9:41, full cellular bars, maximum Wi-Fi connection, and a full battery.](https://docs-assets.developer.apple.com/published/a64d9925fd89d1ccf9f74b347ee622d4/status-bar-messages@2x.png)

### [Navigation bar and Messages header](/design/human-interface-guidelines/messages-for-business#Navigation-bar-and-Messages-header)

The navigation bar — which contains the Messages header — extends to the top of the screen. The system composites the status bar on top of the navigation bar, which lets the navigation bar’s background color show through. You can use the same custom colors for the navigation bar background and buttons as you use in the rest of your Messages for Business UI. For guidance, see [Color](/design/human-interface-guidelines/messages-for-business#Color)
.

To make your screenshots look realistic, include these items in your navigation bar and Messages header:

* A back button at the far left
* An Info button at the far right
* Your company logo centered between the back and Info buttons
* Your company name, followed by a transparent checkmark inside a white or black circle, centered below the logo

Use a maximum height of 27 pixels for your logo and 14 pixels for your company name and checkmark. For example, your navigation bar and Messages header might look something like this:

![An illustration of a Messages for Business navigation bar on iPhone. Callouts denote a logo height of 27 pixels and a company name and checkmark height of 14 pixels.](https://docs-assets.developer.apple.com/published/10f8dfbc094f6c72340a152aa234ecbb/nav-bar-message-header@2x.png)

### [Message bubbles](/design/human-interface-guidelines/messages-for-business#Message-bubbles)

Message bubbles appear in the conversation area of the Messages app screen. All conversation content, including text, links, and images, must appear within message bubbles.

To help people understand the flow of the conversation in your screenshot, it’s important to be consistent about how you use message bubbles to represent the participants. Use the following values for the bubble background color, the direction of its tail, and the text color. Use SF Pro Regular for all text.



| Participant | Background color | Tail direction | Text color |
| --- | --- | --- | --- |
| Customer | #848E99 | Right | White |
| Agent | #E6E5EB | Left | Black |

If you show only two message bubbles, use 4 points of vertical space to separate them. If you need to show more message bubbles, or more than one Send action, use 1 pixel to separate bubbles.

For a message bubble that contains only text, use the following values to determine its height.



| Rows of text | Message bubble height (pixels) |
| --- | --- |
| 1 | 36 |
| 2 | 57 |
| 3 | 76 |
| 4 | 96 |
| 5 | 118 |

For guidance on creating realistic conversations, see [Automated messaging](https://register.apple.com/resources/messages/messaging-documentation/ux-design#automated-messaging)
.

You might also want your screenshot to show message bubbles that include icons or rich links that display images or videos. When a message bubble includes a rich link, the title and the website URL appear below the image or video. An icon appears by itself in a message bubble. If you want to include images or icons in your message bubbles, use the following values to determine the bubble’s size.



| Content | Maximum content size (pixels) | Message bubble size (pixels) |
| --- | --- | --- |
| Image (with tail) | Large (265x160) | 270x210 |
| Image (without tail) | Large (265x160) | 265x210 |
| Image (with tail) | Extra large (276x160) | 280x210 |
| Icon | Medium (280x85) | 280x85 |
| Icon | Small (60x33) | 280x65 |

### [The compose area](/design/human-interface-guidelines/messages-for-business#The-compose-area)

The compose area appears below the conversation area and above the keyboard, if one is present. From the left, the compose area includes a camera button and an apps button, followed by a text input field, which contains placeholder text and the microphone glyph. Use *To: MyCompanyName* for the placeholder text and use dark gray (#868E99) for the microphone glyph.

![An illustration of the compose bar below a message on iPhone. The bar contains a camera button, an apps button, and an address view that includes a microphone button and the placeholder text ’To: Company Name’.](https://docs-assets.developer.apple.com/published/038ce96858790f8115df35542a83a1cb/compose-no-typing-indicator@2x.png)If you want to include the keyboard in your screenshot, add the blue typing indicator to the text input field, using #007AFF for the color. If you also want to show what the customer is typing, move the typing indicator to the right of the input text and replace the microphone glyph with the Send button.

![An illustration of the compose bar below a message and above an onscreen keyboard on iPhone. The bar contains a camera button, an apps button, and an address view that includes a microphone button, the placeholder text ’To: Company Name’, and the typing indicator to the left of the placeholder text.](https://docs-assets.developer.apple.com/published/b2b711c3f7b4db2f4924397e5b35b772/compose-typing-indicator@2x.png)[Platform considerations](/design/human-interface-guidelines/messages-for-business#Platform-considerations)
-----------------------------------------------------------------------------------------------------------

*No additional considerations for iOS, iPadOS, macOS, visionOS, or watchOS. Not supported in tvOS.*

[Resources](/design/human-interface-guidelines/messages-for-business#Resources)
-------------------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/messages-for-business#Related)

[Messages for Business Accounts](https://register.apple.com/resources/messages/messaging-documentation/)


[Change log](/design/human-interface-guidelines/messages-for-business#Change-log)
---------------------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| May 2, 2023 | Consolidated guidance into one page. |

