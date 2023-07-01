Tap to Pay on iPhone
====================

Tap to Pay on iPhone lets merchants accept contactless payments using an app on their iPhone, without having to connect external hardware.![A sketch of progressively larger curved lines extending toward the right within a circle, suggesting Tap to Pay on iPhone. The image is overlaid with rectangular and circular grid lines and is tinted blue to subtly reflect the blue in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/8dc8e961db3023f79bbdaaec49b8c194/technologies-TapToPay-intro@2x.png)

In addition to accepting in-person contactless payments, Tap to Pay on iPhone also lets merchants issue refunds, accept loyalty cards, and validate credit cards, such as when a customer wants to save their card for future use.

Note

Tap to Pay on iPhone works alongside your existing payment-acceptance hardware and accessories.

You can support Tap to Pay on iPhone in an iOS app that you provide to merchants and businesses. Although a merchant’s customers don’t use your app directly, they view some of your app’s screens as they interact with the merchant, so it’s important to follow best practices for visual design and behavior. For high-level developer and business guidance, see [Tap to Pay on iPhone](https://developer.apple.com/tap-to-pay/)
.

[Best practices](/design/human-interface-guidelines/tap-to-pay-on-iphone#Best-practices)
----------------------------------------------------------------------------------------

**Make it easy for merchants to accept Tap to Pay on iPhone terms and conditions before they begin a customer interaction.** Merchants must accept the terms and conditions before you perform the initial configuration on their devices, so it’s most convenient when they can do so before they begin a checkout or other customer-facing flow. To make sure merchants understand this requirement, consider describing it during app launch; for an example, see [Marketing guidelines](https://developer.apple.com/tap-to-pay/marketing-guidelines/#in-your-app)
.

**Present the Tap to Pay on iPhone terms and conditions to the appropriate business representative.** Specifically, if your app supports both administrator and nonadministrator accounts, be sure to present the terms and conditions to an administrator. If a nonadministrator tries to activate the feature, present a message explaining that administrator access is required.

**Educate merchants on how to use Tap to Pay on iPhone before they interact with their customers.** For example, you could display brief instructional content while the initial configuration step completes, showing how to accept payment from cards, digital wallets, Apple Watch, and other wearable devices. After configuration completes, encourage merchants to try a refundable test transaction. Also consider making your educational content easy for merchants to view at any time so they can refer to it when they want. To view some sample educational materials, see [Communicating to merchants](https://developer.apple.com/tap-to-pay/marketing-guidelines/#merchant-communication)
.

**Avoid making merchants wait to use Tap to Pay on iPhone.** In addition to performing the initial per-device configuration — which can take a few minutes — you need to perform a subsequent configuration each time your app becomes frontmost. You can minimize potential wait times by preparing the feature as soon as your app starts and immediately after each transition to the foreground. For developer guidance, see [`prepare(using:)`](/documentation/ProximityReader/PaymentCardReader/prepare(using:))
.

**Make sure the Tap to Pay on iPhone checkout option is available even if configuration is continuing in the background.** Merchants must always be able to select the Tap to Pay on iPhone checkout option during a checkout flow. If configuration is ongoing, let merchants select the checkout option and then display a [progress indicator](https://developer.apple.com/design/human-interface-guidelines/progress-indicators#iOS-iPadOS)
 — avoid waiting for configuration to complete before making the option available.

**Make it easy for merchants to switch between Tap to Pay on iPhone and the hardware accessories you support.** Because your support for Tap to Pay on iPhone is separate from your support for a hardware accessory like a Bluetooth chip and PIN reader, you can help merchants set up both payment-acceptance solutions at the same time. After setup, make sure merchants can choose the appropriate solution during a checkout flow without having to visit your settings area.

[Presentation](/design/human-interface-guidelines/tap-to-pay-on-iphone#Presentation)
------------------------------------------------------------------------------------

Tap to Pay on iPhone is a payment-acceptance method, not a payment method like Apple Pay, cash, or credit. It’s important for your app to present the feature correctly so that merchants can represent it correctly to their customers.

During a Tap to Pay on iPhone experience, the system presents screens that help customers participate in the process. You need to supply information for the system to display in these screens, such as the merchant name and icon — available through the payment card reader token you receive from your payment service provider (PSP) — and the final transaction amount.

**Don’t confuse Apple Pay with Tap to Pay on iPhone.** Customers can use Tap to Pay on iPhone with Apple Pay, but it’s essential to distinguish the acceptance method from the payment method. In particular, avoid displaying an Apple Pay button near a Tap to Pay on iPhone button in your app.

**Make sure you know the final amount that customers need to pay before merchants initiate the Tap to Pay on iPhone experience.** For example, if your app supports tipping or other customer interactions that can change the total, it’s important to ensure that merchants perform these interactions before they initiate Tap to Pay on iPhone. As much as possible, display the final amount customers need to pay in the Tap to Pay on iPhone screen.

**If your app supports multiple payment-acceptance methods, make the Tap to Pay on iPhone button easy to find.** As much as possible, avoid making merchants scroll to access the feature. If your app doesn’t support other payment-acceptance options, you can open Tap to Pay on iPhone automatically when checkout begins.

**For the button that activates the feature, prefer the label “Tap to Pay on iPhone” or — if space is constrained — “Tap to Pay.”** Alternatively, if you use icons in buttons that activate other acceptance methods, use the `wave.3.right.circle` or `wave.3.right.circle.fill` [SF Symbols](/design/human-interface-guidelines/sf-symbols)
 in your Tap to Pay on iPhone button. Regardless of which design you choose, be sure to avoid including the Apple logo.

![An illustration of a 'Tap to Pay' button containing an icon. The button correctly includes a wave symbol followed by the words 'Tap to Pay on iPhone'.](https://docs-assets.developer.apple.com/published/2847ded54a90ef597b34b7ff333e47b2/tap-to-pay-on-iphone-symbol-correct@2x.png)

![A checkmark in a circle to indicate correct usage.](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark@2x.png)

![An illustration of a 'Tap to Pay' button containing an icon. The button incorrectly includes the Apple logo followed by the words 'Tap to Pay on iPhone'.](https://docs-assets.developer.apple.com/published/cb1cece72b73adf6bed5429864699859/tap-to-pay-on-iphone-logo-incorrect@2x.png)

![An X in a circle to indicate incorrect usage.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout@2x.png)

If Tap to Pay on iPhone is the only payment-acceptance method you support, you can reuse your existing Charge or Checkout buttons to activate Tap to Pay on iPhone, if necessary.

[Additional interactions](/design/human-interface-guidelines/tap-to-pay-on-iphone#Additional-interactions)
----------------------------------------------------------------------------------------------------------

To support situations like looking up a past transaction or retaining card information to ensure future payment, Tap to Pay on iPhone lets merchants read a payment card when there’s no transaction amount.

When people have other types of NFC-compatible cards or passes in Apple Wallet — such as loyalty, discount, and points cards — Tap to Pay on iPhone lets merchants read these items at the same time as they read a payment card or independently.

**If you support an independent loyalty card transaction, distinguish this flow from a payment-acceptance flow that uses Tap to Pay on iPhone.** For example, give merchants a separate button to initiate a loyalty card transaction, using a button label that helps them avoid choosing the wrong one by mistake.

![An illustration of a button correctly titled 'Loyalty Card'.](https://docs-assets.developer.apple.com/published/e586a72bca99cdaa8c68fb4b99c8e209/loyalty-card@2x.png)

![An illustration of a button correctly titled 'Tap to Pay on iPhone.](https://docs-assets.developer.apple.com/published/e525ae8a6537cce25a2ec03aace958f1/tap-to-pay-on-iphone@2x.png)

![A checkmark in a circle to indicate correct usage.](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark@2x.png)

![An illustration of a button incorrectly titled 'Tap to Pay on iPhone - Loyalty'.](https://docs-assets.developer.apple.com/published/72070690d8e7d35c7c79169e018faa39/tap-to-pay-on-iphone-loyalty@2x.png)

![An illustration of a button incorrectly titled 'Tap to Pay on iPhone - Payment'.](https://docs-assets.developer.apple.com/published/7ce2b537d4ed07256ff868805ea5f58a/tap-to-pay-on-iphone-payment@2x.png)

![An X in a circle to indicate incorrect usage.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout@2x.png)

[Platform considerations](/design/human-interface-guidelines/tap-to-pay-on-iphone#Platform-considerations)
----------------------------------------------------------------------------------------------------------

*No additional considerations for iOS. Not supported in iPadOS, macOS, tvOS, visionOS, or watchOS.*

[Resources](/design/human-interface-guidelines/tap-to-pay-on-iphone#Resources)
------------------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/tap-to-pay-on-iphone#Related)

[Tap to Pay on iPhone Marketing guidelines](https://developer.apple.com/tap-to-pay/marketing-guidelines/)


#### [Developer documentation](/design/human-interface-guidelines/tap-to-pay-on-iphone#Developer-documentation)

[Configuring Tap to Pay on iPhone](/documentation/ProximityReader/configuring-tap-to-pay-on-iPhone)


[Change log](/design/human-interface-guidelines/tap-to-pay-on-iphone#Change-log)
--------------------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| March 3, 2023 | Enhanced guidance for educating merchants and improving their experience. |
| September 14, 2022 | Refined guidance on preparing Tap to Pay on iPhone and helping merchants learn how to use the feature. |

