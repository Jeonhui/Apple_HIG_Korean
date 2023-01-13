# **[technologies] tap-to-pay-on-iphone**

# Tap to Pay on iPhone lets merchants accept contactless payments using an enabled app on their iPhone, without having to connect external hardware.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-TapToPay-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-TapToPay-intro_2x.png)

In addition to accepting in-person contactless payments, Tap to Pay on iPhone also lets merchants issue refunds, accept loyalty cards, and validate credit cards, such as when a customer wants to save their card for future use.

**NOTE**Tap to Pay on iPhone works alongside your existing payment acceptance hardware and accessories.

You can enable Tap to Pay on iPhone in an iOS app that you provide to merchants and businesses. Although a merchant’s customers don’t use your app directly, they view some of your app’s screens as they interact with the merchant, so it’s important to follow best practices for visual design and behavior. For high-level developer and business guidance, see [Tap to Pay on iPhone](https://developer.apple.com/tap-to-pay/).

# **Best practices**

**Make sure merchants accept Tap to Pay on iPhone terms and conditions before they begin a customer interaction.** Merchants must accept the terms and conditions before you perform the initial configuration on their devices, so it’s important that they do so before they begin a checkout or other customer-facing flow. For developer guidance, see [Configuring Tap to Pay on iPhone](https://developer.apple.com/documentation/proximityreader/configuring-tap-to-pay-on-iphone).

**Present the Tap to Pay on iPhone terms and conditions to the appropriate business representative.** Specifically, if your app supports both administrator and nonadministrator accounts, be sure to present the terms and conditions to an administrator. If a nonadministrator tries to activate the feature, present a message explaining that administrator access is required.

**Avoid making merchants wait to use Tap to Pay on iPhone.** In addition to performing the initial per-device configuration — which can take a few minutes — you need to perform a subsequent configuration each time your app becomes frontmost. You can minimize potential wait times by preparing the feature as soon as your app starts and immediately after each transition to the foreground. For developer guidance, see [prepare(using:)](https://developer.apple.com/documentation/proximityreader/paymentcardreader/prepare(using:)).

**Help merchants gauge how long a configuration is likely to take.** For example, consider displaying a [progress bar](https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators#ios-ipados).

**Consider helping merchants learn how to use Tap to Pay on iPhone before they interact with their customers.** For example, you could present screens that show how to accept payment from cards, digital wallets, and wearable devices like Apple Watch. You might want to display brief instructional content while the initial configuration step completes.

**Make it easy for merchants to switch between Tap to Pay on iPhone and the hardware accessories you support.** Because your support for Tap to Pay on iPhone is separate from your support for a hardware accessory like a Bluetooth chip and PIN reader, you can help merchants set up both payment acceptance solutions at the same time. After setup, make sure merchants can choose the appropriate solution during a checkout flow without having to visit your settings area to do so.

# **Presentation**

Tap to Pay on iPhone is a payment acceptance method; it isn’t a payment method like Apple Pay, cash, or credit. It’s important for your app to present the feature correctly so that merchants can in turn represent it correctly to their customers.

During a Tap to Pay on iPhone experience, the system presents screens that help customers participate in the process. You need to supply information for the system to display in these screens, such as the merchant name and icon — available through the payment card reader token you receive from your payment service provider (PSP) — and the final transaction amount.

**Don’t confuse Apple Pay with Tap to Pay on iPhone.** Customers can use Tap to Pay on iPhone with Apple Pay, but it’s essential to distinguish the acceptance method from the payment method. In particular, avoid displaying an Apple Pay button near a Tap to Pay on iPhone button in your app.

**Make sure you know the final amount that customers need to pay before enabling the Tap to Pay on iPhone experience.** For example, if your app supports tipping or other customer interactions that can change the total, it’s important to ensure that merchants perform these interactions before they initiate Tap to Pay on iPhone. As much as possible, display the final amount customers need to pay in the Tap to Pay on iPhone screen.

**If your app supports multiple payment acceptance methods, make the Tap to Pay on iPhone button easy to find.** As much as possible, avoid making merchants scroll to access the feature. If your app doesn’t support other payment acceptance options, you can open Tap to Pay on iPhone automatically when checkout begins.

**For the button that activates the feature, prefer the label “Tap to Pay on iPhone” or — if space is constrained — “Tap to Pay.”** Alternatively, if you use icons in buttons that enable other acceptance methods, use the `wave.3.right.circle` or `wave.3.right.circle.fill` [symbol](https://developer.apple.com/design/human-interface-guidelines/foundations/sf-symbols) in your Tap to Pay on iPhone button. Regardless of which design you choose, be sure to avoid including the Apple logo.

![https://developer.apple.com/design/human-interface-guidelines/technologies/tap-to-pay-on-iphone/images/tap-to-pay-on-iphone-symbol-correct_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/tap-to-pay-on-iphone/images/tap-to-pay-on-iphone-symbol-correct_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/tap-to-pay-on-iphone/images/tap-to-pay-on-iphone-logo-incorrect_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/tap-to-pay-on-iphone/images/tap-to-pay-on-iphone-logo-incorrect_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)

If Tap to Pay on iPhone is the only payment acceptance method you support, you can re-use existing “Charge” or “Checkout” buttons to activate Tap to Pay on iPhone, if necessary.

# **Additional interactions**

To support situations like looking up a past transaction or retaining card information to ensure future payment, Tap to Pay on iPhone lets merchants read a payment card when there’s no transaction amount.

When people have other types of NFC-enabled cards or passes in Apple Wallet — such as loyalty, discount, and points cards — Tap to Pay on iPhone lets merchants read these items at the same time as they read a payment card or independently.

**If you support an independent loyalty card transaction, distinguish this flow from a payment acceptance flow that uses Tap to Pay on iPhone.** For example, give merchants a separate button to initiate a loyalty card transaction, using a button label that helps them avoid choosing the wrong one by mistake.

![https://developer.apple.com/design/human-interface-guidelines/technologies/tap-to-pay-on-iphone/images/loyalty-card_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/tap-to-pay-on-iphone/images/loyalty-card_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/tap-to-pay-on-iphone/images/tap-to-pay-on-iphone_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/tap-to-pay-on-iphone/images/tap-to-pay-on-iphone_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/checkmark_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/tap-to-pay-on-iphone/images/tap-to-pay-on-iphone-loyalty_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/tap-to-pay-on-iphone/images/tap-to-pay-on-iphone-loyalty_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/technologies/tap-to-pay-on-iphone/images/tap-to-pay-on-iphone-payment_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/tap-to-pay-on-iphone/images/tap-to-pay-on-iphone-payment_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/crossout_2x.png)