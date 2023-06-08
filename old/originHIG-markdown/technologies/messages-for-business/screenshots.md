# **[technologies-messages-for-business] screenshots**

By creating screenshots to display on your website or in emails, you can show customers the benefits of using Messages for Business to communicate with your company.

![https://developer.apple.com/design/human-interface-guidelines/technologies/messages-for-business/images/rich-link-yes_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/messages-for-business/images/rich-link-yes_2x.png)

Although you can create custom screenshots from scratch, the easiest method is to download the Messages for Business templates from [Apple Design Resources](https://developer.apple.com/design/resources/#technologies) and edit them as needed. These templates include components — such as a message list, conversation view, time picker, and list picker — and symbols. You can also download an iPhone 11 Pro device frame in which to display the screenshots.

Regardless of how you choose to create your screenshots, ensure that they look good and depict conversations accurately. To help make screenshots look realistic, use SF Pro Regular for conversation text (you can download the San Francisco family of fonts [here](https://developer.apple.com/fonts/)).

# **Status bar**

The system-provided status bar appears at the top edge of the screen and displays information like current time, cellular carrier, network connection status, and battery level. The status bar’s background is transparent by default, and the information it displays can be light or dark, depending on the appearance of the content behind it. It’s important to include the status bar in the screenshots you create, because people expect to see it in a messaging experience.

For consistency, use the following values in every status bar you create:

- Time is 9:41. Use SF Pro Regular and don’t add a.m. or p.m.
- Cellular and Wi-Fi icons show maximum connectivity.
- Battery is full and doesn’t include the charging glyph.

![https://developer.apple.com/design/human-interface-guidelines/technologies/messages-for-business/images/status-bar_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/messages-for-business/images/status-bar_2x.png)

# **Navigation bar and Messages header**

The navigation bar — which contains the Messages header — extends to the top of the screen. The system composites the status bar on top of the navigation bar, which lets the navigation bar’s background color show through. You can use the same custom colors for the navigation bar background and buttons as you use in the rest of your Messages for Business UI. For guidance, see [Color](https://developer.apple.com/design/human-interface-guidelines/technologies/messages-for-business/color).

To make your screenshots look realistic, include these items in your navigation bar and Messages header:

- A back button at the far left
- An Info button at the far right
- Your company logo centered between the back and Info buttons
- Your company name, followed by a transparent checkmark inside a white or black circle, centered below the logo

Use a maximum height of 27 pixels for your logo and 14 pixels for your company name and checkmark. Your navigation bar and Messages header should look something like this:

![https://developer.apple.com/design/human-interface-guidelines/technologies/messages-for-business/images/nav-bar-message-header_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/messages-for-business/images/nav-bar-message-header_2x.png)

# **Message bubbles**

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

For guidance on creating realistic conversations, see [Automated messaging](https://register.apple.com/resources/messages/messaging-documentation/ux-design#automated-messaging).

You might also want your screenshot to show message bubbles that include icons or rich links that display images or videos. When a message bubble includes a rich link, the title and the website URL appear below the image or video. An icon appears by itself in a message bubble. If you want to include images or icons in your message bubbles, use the following values to determine the bubble’s size.

| Content | Maximum content size (pixels) | Message bubble size (pixels) |
| --- | --- | --- |
| Image (with tail) | Large (265x160) | 270x210 |
| Image (without tail) | Large (265x160) | 265x210 |
| Image (with tail) | Extra large (276x160) | 280x210 |
| Icon | Medium (280x85) | 280x85 |
| Icon | Small (60x33) | 280x65 |

# **The compose area**

The compose area appears below the conversation area and above the keyboard, if one is present. From the left, the compose area includes a camera button and an apps button, followed by a text input field, which contains placeholder text and the microphone glyph. Use *To: MyCompanyName*for the placeholder text and use dark gray (#868E99) for the microphone glyph.

![https://developer.apple.com/design/human-interface-guidelines/technologies/messages-for-business/images/compose-no-typing-indicator_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/messages-for-business/images/compose-no-typing-indicator_2x.png)

If you want to include the keyboard in your screenshot, add the blue typing indicator to the text input field, using #007AFF for the color. If you also want to show what the customer is typing, move the typing indicator to the right of the input text and replace the microphone glyph with the Send button.

![https://developer.apple.com/design/human-interface-guidelines/technologies/messages-for-business/images/compose-typing-indicator_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/messages-for-business/images/compose-typing-indicator_2x.png)