Sign in with Apple
==================

Sign in with Apple provides a fast, private way to sign into apps and websites, giving people a consistent experience they can trust and the convenience of not having to remember multiple accounts and passwords.![A sketch of the Apple logo, suggesting Sign in with Apple. The image is overlaid with rectangular and circular grid lines and is tinted blue to subtly reflect the blue in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/0e77230e8cf51c67c7d3a883ec8e0373/technologies-SIWA-intro@2x.png)

Supporting Sign in with Apple lets people use the Apple ID they already have to sign in or sign up, and skip filling out forms, verifying email addresses, and choosing passwords. In cases where you choose to ask for a name and email address, people have the option to share a unique, random email address that automatically relays messages to their personal email address. For developer guidance, see [Authentication Services](/documentation/authenticationservices)
.

You can offer Sign in with Apple in every version of your app or website across all platforms — including non-Apple platforms.

Sign in with Apple makes it easy for people to authenticate with Face ID or Touch ID and has two-factor authentication built in for an added layer of security. Apple doesn’t use Sign in with Apple to profile people or their activity in apps.

[Offering Sign in with Apple](/design/human-interface-guidelines/sign-in-with-apple#Offering-Sign-in-with-Apple)
----------------------------------------------------------------------------------------------------------------

Follow these guidelines to offer Sign in with Apple when it’s most convenient for people.

**Ask people to sign in only in exchange for value.** People need to understand why you’re asking them to sign in, so it can work well to display a brief, approachable description of sign-in benefits. For example, you might want to tell people that signing in lets them personalize the app experience, access additional features, or synchronize data.

**Delay sign-in as long as possible.** People often abandon apps when they’re forced to sign in before doing anything useful. Give them a chance to familiarize themselves with your app before making a commitment. For example, a live-streaming app could let people explore available content before signing in to stream something.

**If you require an account, ask people to set it up before offering any sign-in options.** Start by explaining the reasons for requiring an account. Then, after people complete account setup, let them choose a convenient way to sign in to their new account by offering Sign in with Apple and any other sign-in methods you support.

**Consider letting people link an existing account to Sign in with Apple.** When you support this type of linking, people can get the convenience of using Sign in with Apple while maintaining access to the information in an account they’ve already set up. You can offer account linking before or after people sign in to their existing account. For example:

* If people share an email address through Sign in with Apple and it matches the address in an existing account, you can suggest that they link Sign in with Apple to that account.
* If people used an existing user name and password to sign in, you can display an account-linking suggestion in their account’s settings view or another logical place.

**In a commerce app, wait until after people make a purchase before asking them to create an account.** If you support a guest checkout system, give people a quick way to create an account after the transaction completes. For example, if you support Apple Pay, let people create an account on the order confirmation page. In cases where people have already provided their name and email address during the Apple Pay transaction, you don’t need to ask for this information.

![An illustration representing an order confirmation screen on iPhone. The screen includes buttons titled 'Create Account' and 'Sign up with Apple'.](https://docs-assets.developer.apple.com/published/680a71fb0809ed5ff6c66043344bc448/create-account-after-purchase@2x.png)

**As soon as Sign in with Apple completes, welcome people to their new account.** Help people use their new account right away; don’t delay the experience by asking for information that isn’t required.

**Indicate when people are currently signed in.** You can help people confirm their sign-in method by displaying a phrase like “Using Sign in with Apple” in places like a settings or account interface.

[Collecting data](/design/human-interface-guidelines/sign-in-with-apple#Collecting-data)
----------------------------------------------------------------------------------------

People appreciate Sign in with Apple for its privacy and convenience. Although some apps or websites may require additional information — such as a date of birth or a region of residence — it’s essential to minimize your requests for data as people set up an account. Build on the trust that people have in Sign in with Apple by describing why you need additional data and clearly displaying the data you receive.

**Clarify whether the additional data you request is required or just recommended.** If the data is legally or contractually required — such as an agreement to terms of service, country or region of residence, birth date, or information required by a region’s real-identity laws — make sure people understand that they must supply the additional information to complete the setup of their account. If additional data isn’t required but can improve the user experience, make sure people know the request is optional and help them understand the benefits of providing the information.

**Don’t ask people to supply a password.** A key benefit of Sign in with Apple is that people don’t have to create and memorize additional passwords. Unless people have stopped using Sign in with Apple with your app or website, don’t ask for a password.

**Avoid asking for a personal email address when people supply a private relay address.** Using Sign in with Apple, people can choose to share a private relay address that automatically forwards messages to their verified personal email account. It’s essential to respect this choice and avoid overriding it by asking for a personal email address. If you present customer service, retail, or other experiences that request identification via email address, you can:

* Make sure that people can view their private relay address in your app or website
* Direct people to Settings > Apple ID > Password & Security > Apps using Apple ID to retrieve their private relay address
* Use other identifying values, like an order number or phone number collected as part of a purchase

**Give people a chance to engage with your app before asking for optional data.** As people use your app, you can help them discover places where they can benefit from sharing more information with you. For example, you might suggest that they provide a contact phone number if they want real-time text updates, or social network information if they want to play games with friends. If people choose not to provide optional information, don’t prevent them from accessing their account or using all the features of your app.

**Be transparent about the data you collect.** People value knowing how you use the data that they share with you. One way you can be transparent is to welcome people by using the name or email address they shared. Doing this helps establish how you use this information and, for a relay address, shows people where to find it in the future. If you don’t display all the data that people provide, they are likely to wonder why you asked for it.

[Displaying buttons](/design/human-interface-guidelines/sign-in-with-apple#Displaying-buttons)
----------------------------------------------------------------------------------------------

Apple provides several Sign in with Apple buttons you can use to let people set up an account and sign in. If necessary, you can create a custom button to offer Sign in with Apple; for guidelines, see [Creating a custom Sign in with Apple button](/design/human-interface-guidelines/sign-in-with-apple#Creating-a-custom-Sign-in-with-Apple-button)
.

**Prominently display a Sign in with Apple button.** Make a Sign in with Apple button no smaller than other sign-in buttons, and avoid making people scroll to see the button.

### [Using the system-provided buttons](/design/human-interface-guidelines/sign-in-with-apple#Using-the-system-provided-buttons)

When you use the system-provided APIs to create a Sign in with Apple button, you get the following advantages.

* A button that’s guaranteed to use an Apple-approved appearance
* Assurance that the button’s contents maintain ideal proportions as you change its style
* Automatic translation of the button’s title into the language specified by the device
* Support for configuring the button’s corner radius to match the style of your UI (iOS, macOS, and web)
* A system-provided alternative text label that lets VoiceOver describe the button

For developer guidance, see [`ASAuthorizationAppleIDButton`](/documentation/authenticationservices/asauthorizationappleidbutton)
 (iOS, macOS, and tvOS), [`WKInterfaceAuthorizationAppleIDButton`](/documentation/watchkit/wkinterfaceauthorizationappleidbutton)
 (watchOS), and [Displaying Sign in with Apple buttons on the web](/documentation/sign_in_with_apple/displaying_sign_in_with_apple_buttons_on_the_web)
. You can also visit [Sign in with Apple button](https://appleid.apple.com/signinwithapple/button)
 to view and adjust live previews of web-based buttons and get the code.

The system provides several variants of the button title. Depending on the platform on which your content runs, choose the variant that fits the terminology of your sign-in experience and use it consistently throughout your interfaces.

The following button titles are available for iOS, macOS, tvOS, and the web:

![An illustration of a button that includes the Apple logo and text that reads 'Sign in with Apple'.](https://docs-assets.developer.apple.com/published/863d9ef6e161e603ad9e704cc69595ae/apple-id-sign-in-with@2x.png)

![An illustration of a button that includes the Apple logo and text that reads 'Sign up with Apple'.](https://docs-assets.developer.apple.com/published/cde5067f62449142e4dc47927204bf10/apple-id-sign-up-with@2x.png)

![An illustration of a button that includes the Apple logo and text that reads 'Continue with Apple'.](https://docs-assets.developer.apple.com/published/df7fd035fc3362174701f37948de68bc/apple-id-continue-with@2x.png)

For watchOS, the system provides one title:  Sign in.

![An illustration of a button for watchOS, that includes the Apple logo and text that reads 'Sign in'.](https://docs-assets.developer.apple.com/published/9ee61a67054b99cffb311b6a91bfb1ea/apple-id-watch-44mm-no-background@2x.png)

Depending on the platform, the system provides up to three options for the appearance of the Sign in with Apple button: white, white with an outline, and black. Choose the appearance that works best with the background on which the button displays.

#### [White](/design/human-interface-guidelines/sign-in-with-apple#White)

The white style is available on all platforms and the web. Use this style on dark backgrounds that provide sufficient contrast.

![An illustration of a white button correctly positioned on a dark shaded background. The button includes the Apple logo and text that reads 'Sign in with Apple'.](https://docs-assets.developer.apple.com/published/b18f05a794df2613ba009d3f833d2aae/apple-id-white-yes@2x.png)

![A checkmark in a circle to indicate correct usage.](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark@2x.png)

![An illustration of a white button incorrectly positioned on a light shaded background. The button includes the Apple logo and text that reads 'Sign in with Apple'.](https://docs-assets.developer.apple.com/published/c18a6c2d0dc6c0dc1eed94f5aa8b4acd/apple-id-white-no@2x.png)

![An X in a circle to indicate incorrect usage.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout@2x.png)

#### [White with outline](/design/human-interface-guidelines/sign-in-with-apple#White-with-outline)

The white outlined style is available in iOS, macOS, and the web. Use this style on white or light-color backgrounds that don’t provide sufficient contrast with the white button fill. Avoid using this style on a dark or saturated background, because the black outline can add visual clutter; instead, use the [white](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple#White)
 style to contrast with a dark background.

![An illustration of a white, outlined button correctly positioned on a light shaded background. The button includes the Apple logo and text that reads 'Sign in with Apple'.](https://docs-assets.developer.apple.com/published/88258b46aec0f3809090c1a8454db3ee/apple-id-outline-yes@2x.png)

![A checkmark in a circle to indicate correct usage.](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark@2x.png)

![An illustration of a white, outlined button incorrectly positioned on a dark shaded background. The button includes the Apple logo and text that reads 'Sign in with Apple'.](https://docs-assets.developer.apple.com/published/b521a447f4adb38979ec877aeb907be3/apple-id-outline-no@2x.png)

![An X in a circle to indicate incorrect usage.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout@2x.png)

#### [Black](/design/human-interface-guidelines/sign-in-with-apple#Black)

The black style is available on all platforms and the web. Use this style on white or light-color backgrounds that provide sufficient contrast; don’t use it on black or dark backgrounds.

![An illustration of a black button correctly positioned on a light shaded background. The button includes the Apple logo and text that reads 'Sign in with Apple'.](https://docs-assets.developer.apple.com/published/b0043e04142afb92f994908e3f0810ef/apple-id-black-yes@2x.png)

![A checkmark in a circle to indicate correct usage.](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark@2x.png)

![An illustration of a black button incorrectly positioned on a dark shaded background. The button includes the Apple logo and text that reads 'Sign in with Apple'.](https://docs-assets.developer.apple.com/published/975306cce017e397fdad44f47f8b98c3/apple-id-black-no@2x.png)

![An X in a circle to indicate incorrect usage.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout@2x.png)

Unlike the black Sign in with Apple button for other platforms, the watchOS button uses a fill color that’s not fully black. To contrast with the pure black background of Apple Watch, the watchOS button uses the system-defined dark gray appearance.

![An illustration of a dark shaded button for watchOS on a black background, that includes the Apple logo and text that reads 'Sign in'.](https://docs-assets.developer.apple.com/published/5ae333652f48aa188a6df8b1c72c8dad/apple-id-watch-44mm@2x.png)

#### [Button size and corner radius](/design/human-interface-guidelines/sign-in-with-apple#Button-size-and-corner-radius)

**Adjust the corner radius to match the appearance of other buttons in your app.** By default, the Sign in with Apple button has rounded corners. In iOS, macOS, and the web, you can change the corner radius to produce a button with square corners or a pill-shaped button. For developer guidance, see [`cornerRadius`](/documentation/authenticationservices/asauthorizationappleidbutton/3153030-cornerradius)
 (iOS and macOS) and [Displaying Sign in with Apple buttons on the web](/documentation/sign_in_with_apple/displaying_sign_in_with_apple_buttons_on_the_web)
.

![An illustration of a 'Sign in with Apple' button with 90-degree corners.](https://docs-assets.developer.apple.com/published/da3ba479ed2c9d306f4a8b767eb357f3/apple-id-minimum-corner-radii@2x.png)Minimum corner radius![An illustration of a 'Sign in with Apple' button with the default corner radius.](https://docs-assets.developer.apple.com/published/863d9ef6e161e603ad9e704cc69595ae/apple-id-default-corner-radii@2x.png)Default corner radius![An illustration of a 'Sign in with Apple' button with the maximum corner radius, which results in a lozenge-like appearance.](https://docs-assets.developer.apple.com/published/4b0941406e76bdccd4f10b586abc1047/apple-id-maximum-corner-radii@2x.png)Maximum corner radius**Maintain the minimum button size and margin around the button in iOS, macOS, and the web.** Be mindful that the button title may vary in length depending on the locale. Use the following values for guidance.



| Minimum width | Minimum height | Minimum margin |
| --- | --- | --- |
| 140pt (140px @1x, 280px @2x) | 30pt (30px @1x, 60px @2x) | 1/10 of the button’s height |

### [Creating a custom Sign in with Apple button](/design/human-interface-guidelines/sign-in-with-apple#Creating-a-custom-Sign-in-with-Apple-button)

If your interface requires it, you can create a custom Sign in with Apple button for iOS, macOS, or the web. For example, you may want to align logos across multiple sign-in buttons, use buttons that display only a logo, or adjust the button’s font, bezel, or background appearance to coordinate with your UI.

![An illustration that includes two side-by-side partial iPhones showing sign-in screens. The screen on the left includes four stacked buttons: Sign in with Apple, Sign in with X, Sign in with Y, and Sign in with Z. The Sign in with Apple button includes an Apple logo before its title. The Sign in with X button includes a filled circle before its title. The Sign in with Y button includes a filled square before its title. The Sign in with Z button includes a filled triangle before its title. The screen on the right includes a heading that reads 'Sign in with', which appears above a row of four square buttons containing glyphs. The first square button contains the Apple logo. The second square button contains a filled circle. The third square button contains a filled square. The fourth square button contains a filled triangle. The circle, square, and triangle shapes represent a variety of logos.](https://docs-assets.developer.apple.com/published/e4e072ba920fe6ed52f67ca400e9059e/custom-sign-in-screens@2x.png)

Always make sure that people can instantly identify your custom button as a Sign in with Apple button. If your custom button differs too much from the standard one, people may not feel comfortable using it to set up an account or sign in. App Review evaluates all custom Sign in with Apple buttons.

[Apple Design Resources](https://developer.apple.com/design/resources/)
 provides downloadable Apple logo artwork you can use to create custom Sign in with Apple buttons that display either a logo only or a logo and text. The logo files are available in PNG, SVG, and PDF formats, and the artwork for both types of buttons includes both black and white versions. Here are examples of the black and white logo-only art files, each with a background added for visibility.

![A illustration of a black Apple logo within a white square, which is surrounded by a thick, shaded border. The white square represents the minimum amount of clear space between the Apple logo and other interface elements.](https://docs-assets.developer.apple.com/published/c6663e33b5691085e3a9761ee924b071/siwa-black-logo-only@2x.png)

![A illustration of a white Apple logo within a black square, which is surrounded by a thick, light border. The black square represents the minimum amount of clear space between the Apple logo and other interface elements.](https://docs-assets.developer.apple.com/published/881ddae25d4b8ab21dde7d81e2991b7f/siwa-white-logo-only@2x.png)

All downloadable logo files include padding that simplifies positioning the logo in a button. Logo-only logo files include horizontal and vertical padding that ensures the correct proportion of the logo relative to the button. In addition to padding that keeps the logo and button correctly proportioned, logo files for buttons with text also include horizontal padding that provides a minimum margin between the logo and the button’s leading edge and title.

Use only the logo artwork downloaded from [Apple Design Resources](https://developer.apple.com/design/resources/)
; never create a custom Apple logo. As you create a custom Sign in with Apple button, follow these guidelines for using the downloadable logo file:

* Use the logo file to position the Apple logo in a button; never use the Apple logo as a button.
* Match the height of the logo file to the height of the button.
* Don’t crop the logo file.
* Don’t add vertical padding.

To make sure that your custom button is visually consistent with the system-provided Sign in with Apple button, don’t change the following attributes.

* Titles. Use only *Sign in with Apple*, *Sign up with Apple*, or *Continue with Apple*.
* General shape. Buttons that combine the logo with text are always rectangular; logo-only buttons can be circular or rectangular.
* Logo and title colors. Within a button, both items must be either black or white; don’t use custom colors.

To coordinate with your app design, you can change:

* Title font. You can also adjust the font’s weight and size.
* Title case. You can capitalize every letter in the title.
* Background appearance. The overall color needs to remain black or white. If necessary, you can include a subtle texture or gradient to help the button harmonize with your interface.
* Button corner radius. You can use a corner radius value that matches the other buttons in your UI.
* Button bezel and shadow. For example, you can use a stroke to emphasize the button bezel or add a drop shadow.

#### [Custom buttons with a logo and text](/design/human-interface-guidelines/sign-in-with-apple#Custom-buttons-with-a-logo-and-text)

**Choose the format of the logo file based on the height of your button.** Because SVG and PDF are vector-based formats, you can use these files in buttons of any height. Use the PNG files only in buttons that are 44 points tall, which is the default (and recommended) button height in iOS. Logos are available in small, medium, and large sizes, so you can match logo sizes in all the sign-up buttons you display.

**Prefer the system font for the title — that is, Sign in with Apple, Sign up with Apple, or Continue with Apple.** Regardless of the font you choose, the title and button height of your custom button need to use the same proportions that the system uses. Using the system font for example, the title’s font size would be 43% of the button’s height — in other words, the button’s height would be 233% of the title’s font size, rounded to the nearest integer. Here are two examples that show these proportions using different sizes of the system font.

![An illustration of a Sign in with Apple button, with callouts that indicate a button height of 44 points and a font size of 19 points.](https://docs-assets.developer.apple.com/published/967540b79231c55913033f4caa9c91db/left-aligned-correct-proportions-2@2x.png)

![An illustration of a Sign in with Apple button, with callouts that indicate a button height of 56 points and a font size of 24 points.](https://docs-assets.developer.apple.com/published/b1d458fd23bc97395e85defebb79cd37/left-aligned-correct-proportions-1@2x.png)

**In general, preserve the capitalization style of the title.** By default, all variants of the button title capitalize the first word — that is, *Sign* or *Continue* — and *Apple*; all other letters are lowercase. Avoid changing this style unless your interface uses only uppercase.

**Keep the title and logo vertically aligned within the button.** To do this, vertically align the title to the middle of the button, then add the logo image, making sure its height matches the height of the button. Because the logo image includes top and bottom padding, vertically aligning the title in the button ensures that the title, the logo, and the button stay properly aligned.

**Inset the logo if necessary.** If you need to horizontally align the Apple logo with other authentication logos, you can adjust the space between the logo and the button’s leading edge.

**Maintain a minimum margin between the title and the right edge of the button.** Ensure the margin measures at least 8% of the button’s width.

**Maintain the minimum button size and margin around the button.** Be mindful that the button title may vary in length depending on the locale. Use the following values for guidance.



| Minimum width | Minimum height | Minimum margin |
| --- | --- | --- |
| 140 pt (140 px @1x, 280 px @2x) | 30 pt (30 px @1x, 60 px @2x) | 1/10 of the button’s height |

#### [Custom logo-only buttons](/design/human-interface-guidelines/sign-in-with-apple#Custom-logo-only-buttons)

**Choose the format of the logo file based on the size of your button.** The downloadable artwork for logo-only buttons is available in SVG, PDF, and PNG formats. Use the vector-based SVG and PDF formats for buttons of any size; use the PNG format only in buttons that measure 44x44 pt.

**Don’t add horizontal padding to a logo-only image.** A logo-only Sign in with Apple button always has a 1:1 aspect ratio, and the artwork already includes the correct padding on all sides.

**Use a mask to change the default square shape of the logo-only image.** For example, you might want to use a circular or rounded rectangular shape to present all logo-only sign-in buttons. Never crop the Apple-provided artwork to decrease its built-in padding or use the logo by itself, and avoid including additional padding.

![An illustration of a logo-only Sign in with Apple button. The button includes only the Apple logo, and the button has rounded corners.](https://docs-assets.developer.apple.com/published/f5e783edee3a2ab6c5171f121e0e1894/siwa-logo-masked-rounded-rect@2x.png)Rounded rectangle mask![An illustration of a logo-only Sign in with Apple button. The button includes only the Apple logo, and the button has square corners.](https://docs-assets.developer.apple.com/published/7e4610f57c6a5aca09a64dde7756d7b7/siwa-logo-default@2x.png)No mask![An illustration of a logo-only Sign in with Apple button. The button includes only the Apple logo, and the button is circular.](https://docs-assets.developer.apple.com/published/ec7ae1718620f0629595ac57950ef561/siwa-logo-masked-circle@2x.png)Circular mask**Maintain a minimum margin around the button.** Ensure the margin measures at least 1/10 of the button’s height.

[Platform considerations](/design/human-interface-guidelines/sign-in-with-apple#Platform-considerations)
--------------------------------------------------------------------------------------------------------

*No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

[Resources](/design/human-interface-guidelines/sign-in-with-apple#Resources)
----------------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/sign-in-with-apple#Related)

[Sign in with Apple button](https://appleid.apple.com/signinwithapple/button)


#### [Developer documentation](/design/human-interface-guidelines/sign-in-with-apple#Developer-documentation)

[Authentication Services](/documentation/authenticationservices)


[Displaying Sign in with Apple buttons on the web](/documentation/sign_in_with_apple/displaying_sign_in_with_apple_buttons_on_the_web)


#### [Videos](/design/human-interface-guidelines/sign-in-with-apple#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/119/B671AE75-5224-4AA1-BB31-F4CBA7E95342/5002_wide_250x141_1x.jpg) Move beyond passwords](https://developer.apple.com/videos/play/wwdc2021/10106) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/119/AB014534-6C60-4B00-9D7D-E2EDD02E3D6E/5211_wide_250x141_1x.jpg) Simplify sign in for your tvOS apps](https://developer.apple.com/videos/play/wwdc2021/10279) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/48/D792218F-60EA-427D-8034-204243D383C7/2645_wide_250x141_1x.jpg) Introducing Sign In with Apple](https://developer.apple.com/videos/play/wwdc2019/706) 
[Change log](/design/human-interface-guidelines/sign-in-with-apple#Change-log)
------------------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| September 14, 2022 | Refined guidance on supporting existing accounts, helping people set up a new account, and indicating the current sign-in status. Consolidated guidance into one page. |

