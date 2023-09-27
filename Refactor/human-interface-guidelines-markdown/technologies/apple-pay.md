Apple Pay
=========

Apple Pay is a secure, easy way to make payments for physical goods and services — as well as donations and subscriptions — in apps running on iPhone, iPad, Mac, and Apple Watch, and on websites.![A sketch of a dollar sign, suggesting Apple Pay. The image is overlaid with rectangular and circular grid lines and is tinted blue to subtly reflect the blue in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/4ae8b2e3b4d91aa604d2836031526f06/technologies-Apple-Pay-intro@2x.png)

People authorize payments and provide shipping and contact information, using credentials that are securely stored on the device.

Tip

It’s important to understand the difference between Apple Pay and [In-app purchase](/design/human-interface-guidelines/in-app-purchase)
. Use Apple Pay in your app to sell physical goods like groceries, clothing, and appliances; for services such as club memberships, hotel reservations, and tickets for events; and for donations. Use In-App Purchase in your app to sell virtual goods, such as premium content for your app, and subscriptions for digital content.

Apps that accept Apple Pay display an Apple Pay mark wherever available payment options are shown and an Apple Pay button that people tap to bring up a payment sheet. During checkout, the payment sheet can show the credit or debit card linked to Apple Pay, purchase amount (including tax and fees), shipping options, and contact information. People make any necessary adjustments and then authorize payment and complete the purchase.

![A screenshot of a payment sheet that displays details about a purchase, including bank information, shipping address, and the total amount.](https://docs-assets.developer.apple.com/published/6cf5ebcf6d1f2e0f1b88e943ee4cecd9/apple-pay-sheet@2x.png)For developer guidance, see [Apple Pay](/documentation/passkit/apple_pay)
.

Websites that accept Apple Pay incorporate it into the purchasing flow. An Apple Pay mark needs to be shown wherever available payment options are shown and an Apple Pay button lets people view a payment sheet. During checkout, the payment sheet can show the credit or debit card linked to Apple Pay, purchase amount (including tax and fees), shipping options, and contact information. People make any necessary adjustments, authorize payment, and complete the purchase using securely stored credentials on iPhone, iPad, and Macs that include Touch ID or a Magic Keyboard with Touch ID (for a complete list of supported Macs, see [Devices compatible with Apple Pay](https://support.apple.com/en-us/HT208531)
). On other Macs, people confirm the purchase with their nearby iPhone or Apple Watch on which Apple Pay is set up.

![An illustration of a MacBook Pro on the left and an iPhone on the right. The MacBook Pro displays a Safari window that shows an online store with Apple Pay buttons for checking out and adding to a bag. The iPhone displays an Apple Pay payment sheet.](https://docs-assets.developer.apple.com/published/dd757533a7c6981c4932724381e10ad2/apple-pay-hero@2x.png)

All websites that offer Apple Pay must include a privacy statement and adhere to the [Acceptable use guidelines for Apple Pay on the web](https://developer.apple.com/apple-pay/acceptable-use-guidelines-for-websites/)
. For developer guidance, see [Apple Pay on the Web](/documentation/apple_pay_on_the_web)
. For a hands-on demo of Apple Pay on the web, see [Apple Pay on the web interactive demo](https://applepaydemo.apple.com)
.

[Offering Apple Pay](/design/human-interface-guidelines/apple-pay#Offering-Apple-Pay)
-------------------------------------------------------------------------------------

**Offer Apple Pay on all devices that support it.** If the device doesn’t support Apple Pay, don’t present Apple Pay as a payment option.

**If you use Apple Pay APIs to find out whether someone has an active card in Wallet, you must make Apple Pay the primary — but not necessarily sole — payment option everywhere you use the APIs.** For example, you might pre-select Apple Pay as the payment option when you display it alongside other options. For developer guidance, see [`PKPaymentAuthorizationController`](/documentation/passkit/pkpaymentauthorizationcontroller)
 (iOS, watchOS) and [`canMakePaymentsWithActiveCard`](/documentation/apple_pay_on_the_web/applepaysession/1778000-canmakepaymentswithactivecard)
 (web).

**If you also offer other payment methods, offer Apple Pay at the same time.** Feature Apple Pay at least as prominently as the other options on every page or screen that offers or accepts payment methods.

**If you use an Apple Pay button to start the Apple Pay payment process, you must use the Apple-provided API to display it.** Unlike a button graphic, the buttons produced by the API always have the correct appearance and are localized automatically. On devices running older systems that support Apple Pay on the web but don’t include the API, use the recommended CSS to display the buttons on your website, as described in [Displaying Apple Pay Buttons Using CSS](/documentation/apple_pay_on_the_web/displaying_apple_pay_buttons_using_css)
.

**If you use a custom button to start the Apple Pay payment process, make sure your custom button doesn’t display “Apple Pay” or the Apple Pay logo.** In this scenario, you must let people know that you accept Apple Pay by displaying the Apple Pay mark or referencing Apple Pay in text on the same page that displays your payment button.

![An illustration that shows the correct arrangement of the Apple Pay logo above a custom button titled 'Order Now'.](https://docs-assets.developer.apple.com/published/b19a9822ebe73af2ed72bfbdd28ea560/custom-button-yes@2x.png)

![Correct usage](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark@2x.png)

![An illustration that shows the incorrect arrangement of the Apple Pay logo above a custom button titled 'Apple Pay'.](https://docs-assets.developer.apple.com/published/5e2e1ab926f9963755c0547a3621b125/custom-button-no@2x.png)

![Incorrect usage](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout@2x.png)

**Use Apple Pay buttons only to start the Apple Pay payment process and, when appropriate, the Apple Pay set-up process.** When people choose an Apple Pay button to make a purchase, but their device doesn’t have Apple Pay set up, they’re given the opportunity to set up Apple Pay. Don’t use Apple Pay buttons in any other ways.

**Don’t hide an Apple Pay button or make it appear unavailable.** If an Apple Pay button can’t be used yet, such as when a product size or color hasn’t been selected, gracefully point out the problem after someone taps or clicks the button.

**Use the Apple Pay mark only to communicate that Apple Pay is accepted.** The Apple Pay mark doesn’t facilitate payment. Never use it as a payment button or position it as a button. When using the Apple Pay mark to indicate Apple Pay as the selected payment method, you can create a separate custom button conforming to your app’s design to initiate the Apple Pay payment.

**Inform search engines that Apple Pay is accepted on your website.** If your website uses semantic markup to provide product details to search engines, list Apple Pay as a payment option.

For app developer guidance, see [Apple Pay](/documentation/passkit/apple_pay)
. For website developer guidance, including how to determine whether Apple Pay on the web is available, see [Apple Pay on the Web](/documentation/apple_pay_on_the_web)
.

[Streamlining checkout](/design/human-interface-guidelines/apple-pay#Streamlining-checkout)
-------------------------------------------------------------------------------------------

**Provide a cohesive checkout experience.** It’s best when the entire checkout flow feels tightly integrated with your app or website. To strengthen people’s perception of integration, use your branding throughout the checkout experience and avoid opening different pages or windows. For website checkout flows in particular, opening new windows during the process can cause confusion and may even lead people to think they’ve been handed off to a different website.

**If Apple Pay is available, assume the person wants to use it.** Consider presenting the Apple Pay button as the first payment option, displaying it larger than other options, or using a line to visually separate it from other choices.

**Accelerate single-item purchases with Apple Pay buttons on product detail pages.** In addition to offering a shopping cart, consider putting Apple Pay buttons on product detail pages so people can purchase an individual item quickly. Purchases initiated in this way need to be for an individual item only, excluding any items that already reside in the shopping cart. If the shopping cart contains an item purchased directly from a product detail page, remove the item from the cart after the purchase is complete.

**Accelerate multi-item purchases with express checkout.** Consider providing an express checkout feature that immediately displays the payment sheet, allowing people to purchase multiple items quickly using a single shipping method and destination. If you offer a coupon or promotional code, you can enhance the express checkout experience by letting people enter it on the payment sheet.

**Collect necessary information, like color and size options, before people reach the Apple Pay button.** When additional information is needed at checkout time — perhaps because the customer forgot to choose an option — gracefully point out the problem and help them correct it. Use highlighting or warning text to identify missing information, and automatically navigate to the problematic field so people can correct it quickly and complete their purchase.

**Collect optional information before checkout begins.** There’s no way to input optional data — like gift messages or delivery instructions — on the payment sheet, so collect this information ahead of time or even after the purchase is complete.

**Gather multiple shipping methods and destinations before showing the payment sheet.** The payment sheet lets people select a single shipping method and destination for an entire order. If your customers can choose different shipping methods and destinations for individual items in an order, collect those details before Apple Pay checkout begins, instead of on the payment sheet.

**For in-store pickup, help people choose a pickup location before displaying the payment sheet.** After a customer chooses the pickup location they want, use the read-only format to display the location’s address on the payment sheet. For developer guidance, see [Displaying a Read-Only Pickup Address](/documentation/passkit/pkpaymentrequest/displaying_a_read-only_pickup_address)
.

**Prefer information from Apple Pay.** Assume that Apple Pay information is complete and up to date. Even if your app or website has existing contact, shipping, and payment information, consider fetching the latest from Apple Pay during checkout to reduce potential corrections.

**Avoid requiring account creation prior to purchase.** If you want people to register for an account, ask them to do so on the order confirmation page. Prepopulate as many registration fields as possible using information provided by the payment sheet during checkout.

![An illustration of an order confirmation screen on iPhone. The screen contains a button for creating an account and a button for signing up with Apple Pay.](https://docs-assets.developer.apple.com/published/0c5bcc6893b93e48a9d28c2c91dadb3b/payment-sheet-before-account@2x.png)

**Report the result of the transaction so that people can view it in the payment sheet.** In failure cases, the payment sheet can display the errors that you provide, so people can take steps to fix the problem.

**Display an order confirmation or thank-you page.** After the payment sheet shows the result of the transaction, display an order confirmation page to thank people for their purchase, provide details about when the order will ship, and indicate how to check its status. Listing Apple Pay on the confirmation page isn’t necessary, but if you do, show it after the last four digits of the account used to process the transaction or as a separate note. For example, ”1234 (Apple Pay)” or ”Paid with Apple Pay.”

### [Customizing the payment sheet](/design/human-interface-guidelines/apple-pay#Customizing-the-payment-sheet)

**Only present and request essential information.** People may get confused or have privacy concerns if the payment sheet includes extraneous information. For example, it makes sense to see a contact email address but not a shipping address if the purchase is a gift card that will be delivered electronically. Showing or asking for a shipping address in this scenario may give the false impression that something will be physically delivered.

**Display the active coupon or promotional code, or give people a way to enter it.** For example, if people can enter a code before the payment sheet appears, displaying it on the sheet can reassure them that the code works as they expect. Alternatively, allowing code entry on the payment sheet can be particularly beneficial in an express checkout flow.

**Let people choose the shipping method in the payment sheet.** To the extent space permits, show a clear description, a cost, and, optionally, an estimated delivery or pickup date — or range of dates — for each available option. In iOS 15 and later, you can take advantage of the shipping method’s calendar and time-zone support to provide accurate delivery or pickup information, regardless of the customer’s current location. For developer guidance, see [`PKDateComponentsRange`](/documentation/passkit/pkdatecomponentsrange)
.

**For in-store pickup, consider letting people choose a pickup window that works for them.** You can use the shipping method to supply a range of dates and times from which people can choose.

**Use line items to explain additional charges, discounts, pending costs, add-on donations, recurring, and future payments.** A line item includes a label and cost; a line item for a recurring payment can also include a frequency. Don’t use line items to show an itemized list of products that make up the purchase. For developer guidance, see [`paymentSummaryItems`](/documentation/passkit/pkpaymentrequest/1619231-paymentsummaryitems)
; for guidance on donations, see [Supporting donations](/design/human-interface-guidelines/apple-pay#Supporting-donations)
.

* [iOS](#)
* [Web](#)
![A screenshot of an in-app payment sheet that includes an additional charge for gift wrap and a credit applied for a coupon.](https://docs-assets.developer.apple.com/published/b3d9d7f7a3968b37723a73f7332a3ec8/payment-sheet-ios@2x.png)![A screenshot of a webpage payment sheet that includes an additional charge for gift wrap and a credit applied for a coupon.](https://docs-assets.developer.apple.com/published/ff1b8604f18eb85fb8b6cf4662399b5b/payment-sheet-web@2x.png)

**Keep line items short.** Make line items specific and easily understandable at a glance. Whenever possible, fit line items on a single line.

**Provide a business name after the word *Pay* on the same line as the total.** Use the same business name people will see when they look for the charge on their bank or credit card statement. This provides reassurance that payment is going to the right place. For example, Pay [*Business\_Name*].

**If you’re not the end merchant, specify both your business name and the end merchant’s name in the payment sheet.** There are a few ways your app, App Clip, or website might help people make a purchase from an end merchant that’s unrelated to your company. For example, a marketplace app can help people make a purchase from an end merchant they might not recognize. Another example is an app that offers a self-checkout service people can use to pay for an item in an end merchant’s physical store without visiting the store’s checkout counter. In scenarios like these, people might not realize two businesses are involved in the transaction, so it’s essential to name both businesses and clarify their roles. When your app acts as an intermediary for an end merchant, clearly and succinctly describe the situation in the Pay line of the payment sheet, using something like Pay [*End\_Merchant\_Business\_Name* (via *Your\_Business\_Name*)].

**Clearly disclose when additional costs may be incurred after payment authorization.** In some cases, the total cost may be unknown at checkout time. For example, the price of a car ride based on distance or time might change after checkout. Or, a customer might want to add a tip after a product is delivered. In situations like these, and when local regulations allow, you can provide a clear explanation in the payment sheet and a subtotal marked as Amount Pending. If you’re preauthorizing a specific amount, be sure the payment sheet accurately reflects this information.

**Handle data entry and payment errors gracefully.** If an error occurs during checkout, help people resolve it quickly so they can complete their transaction. For related guidance, see [Data validation](/design/human-interface-guidelines/apple-pay#Data-validation)
.

### [Displaying a website icon](/design/human-interface-guidelines/apple-pay#Displaying-a-website-icon)

Many websites provide an icon that can display with bookmarks, in URL fields, or on a device’s Home screen. Websites that support Apple Pay can display this icon in a summary view and in the payment sheet of the connected device that’s used to authorize payment. The icon provides visual reassurance that payment is going to the right place.

If your website supports Apple Pay, provide an icon in the following sizes for use in the summary view and the payment sheet:



| @2x | @3x |
| --- | --- |
| 60x60 pt (120x120 px @2x) | 60x60 pt (180x180 px @3x) |

![An illustration of an Apple Pay payment sheet on iPhone, which shows a website icon above the payment details.](https://docs-assets.developer.apple.com/published/69ae379313b720a151bf5eda6edc712f/web-icon-payment@2x.png)

[Handling errors](/design/human-interface-guidelines/apple-pay#Handling-errors)
-------------------------------------------------------------------------------

Provide clear, actionable guidance when problems occur during checkout or payment processing, so people can resolve problems quickly and complete their transaction.

### [Data validation](/design/human-interface-guidelines/apple-pay#Data-validation)

Your app or website can respond to user input when the payment sheet appears, when people change certain field values on the payment sheet, and after they authenticate the transaction. Use these opportunities to check for data entry problems and to provide clear and consistent messaging.

* [iOS](#)
* [Web](#)
![A screenshot of an in-app Apple Pay payment sheet on iPhone that shows an error with the shipping address.](https://docs-assets.developer.apple.com/published/20ce86c04c37e883ee5f02428240a540/pay-sheet-error-ios@2x.png)Payment sheet error messaging![A screenshot of an in-app shipping screen on iPhone. The screen denotes the zip code doesn't match the city for the home address. Options exist to select or add a different shipping address.](https://docs-assets.developer.apple.com/published/1785ee5f59a1eab5cd0bc6e60970ef29/detail-view-error-ios@2x.png)Custom detail view error messaging![A screenshot of a webpage Apple Pay payment sheet that shows an error with the shipping address.](https://docs-assets.developer.apple.com/published/64b2f25c1f6459308dbd863cbb87cfe2/pay-sheet-error-web@2x.png)Payment sheet error messaging![A screenshot of a webpage Apple Pay payment sheet that shows an error with the shipping address. An overlay appears over the payment sheet and denotes the zip code doesn't match the city for the home address. Options exist to select a different shipping address or edit the shipping address.](https://docs-assets.developer.apple.com/published/edaa7eca0b60819fa6e32052e28bc6f0/detail-view-error-web@2x.png)Custom detail view error messagingWhen data is invalid, system-provided error messaging calls attention to relevant fields on the payment sheet. People can choose a field to view additional details and resolve the problem. Provide customized error messages for the detail view that appears when people choose a problematic field.

For developer guidance, see [`PKPaymentAuthorizationViewControllerDelegate`](/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate)
 (iOS, watchOS) and [Apple Pay on the Web](/documentation/apple_pay_on_the_web)
 (web).

Note

For privacy reasons, your app or website has limited access to data until people attempt to authorize a transaction. Prior to authorization, only the card type and a redacted shipping address are accessible. It’s critical to display errors when authorization fails, but to the extent possible, you also need to attempt to validate available information and report problems before authorization.

**Avoid forcing compliance with your business logic.** Design a data validation process that’s intelligent enough to ignore irrelevant data and infer missing data whenever possible. For example, if your app requires a five-digit zip code but someone enters a Zip+4 code, ignore the additional digits rather than asking for a correction. Let people enter phone numbers in multiple formats — such as with and without dashes, and with and without a country code — without producing an error.

**Provide accurate status reporting to the system.** When a problem occurs, it’s essential that your app or website accurately indicate the type of problem so the system can show the most relevant error message on the payment sheet. This is done by accompanying your custom error message with the correct status code. For developer guidance, see [`PKPaymentError`](/documentation/passkit/pkpaymenterror)
 (iOS, watchOS) and [Apple Pay Status Codes](/documentation/apple_pay_on_the_web/apple_pay_js_api/apple_pay_status_codes)
 (web).

**Succinctly and specifically describe the problem when data is invalid or incorrectly formatted.** Reference the relevant field and indicate exactly what’s expected. For example, if people enter an invalid zip code, instead of showing “Address is invalid,” show a specific message like “Zip code doesn’t match city.” If the shipping address is unserviceable, indicate why with a message like “Shipping not available for this state.” Use noun phrases with sentence-style capitalization and no ending punctuation. Aim to keep messages at 128 characters or fewer to avoid truncation.

### [Payment processing](/design/human-interface-guidelines/apple-pay#Payment-processing)

**Handle interruptions correctly.** A user-driven event like a cancellation or a system-driven event like a timeout could cause an interruption in the payment flow, resulting in the payment sheet being dismissed. When such an event occurs, you must cancel any in-progress payment. After the payment sheet dismisses, people can restart the process by choosing the Apple Pay button again. For developer guidance, see [`PKPaymentAuthorizationViewControllerDelegate`](/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate)
 (iOS, watchOS) and [`oncancel`](/documentation/apple_pay_on_the_web/applepaysession/1778029-oncancel)
 (web).

[Supporting subscriptions](/design/human-interface-guidelines/apple-pay#Supporting-subscriptions)
-------------------------------------------------------------------------------------------------

Your app or website can use Apple Pay to request authorization for recurring fees. A recurring fee can be a fixed amount, such as a monthly movie ticket subscription, or — when local regulations allow — a variable amount like a weekly grocery order. The initial authorization can also include discounts and additional fees.

* [iOS](#)
* [Web](#)
![A screenshot of an in-app Apple Pay payment sheet for a fixed subscription, which includes a monthly amount.](https://docs-assets.developer.apple.com/published/37bfe5244a27c0a332ee36b9f2e451b2/fixed-subscription-ios@2x.png)Fixed subscription![A screenshot of an in-app Apple Pay payment sheet for a variable subscription, which includes the text 'Amount Pending'.](https://docs-assets.developer.apple.com/published/f2ed1136a25038be1576876a9a90d757/variable-subscription-ios@2x.png)Variable subscription (where local regulations allow)![A screenshot of a webpage Apple Pay payment sheet for a fixed subscription, which includes a monthly amount.](https://docs-assets.developer.apple.com/published/6875490a9fda307bdd4183611f87537f/fixed-subscription-web@2x.png)Fixed subscription![A screenshot of a webpage Apple Pay payment sheet for a variable subscription, which includes the text 'Amount Pending'.](https://docs-assets.developer.apple.com/published/ac233da107d9cf6662a2385b5ed181ee/variable-subscription-web@2x.png)Variable subscription (where local regulations allow)**Clarify subscription details before showing the payment sheet.** Before asking people to authorize a recurring payment, make sure they fully understand the billing frequency and any other terms of service. You can reiterate the billing frequency on the payment sheet.

**Include line items that reiterate billing frequency, discounts, and additional upfront fees.** Use these line items to remind people what they’re authorizing. If no payment is required at authorization time, clearly disclose when billing will occur.

* [iOS](#)
* [Web](#)
![A screenshot of an in-app Apple Pay payment sheet for a fixed subscription that doesn’t require payment until after the first month. The total shows a zero dollar amount.](https://docs-assets.developer.apple.com/published/013846a00db9da788e1b943a1564c90c/no-payment-required-ios@2x.png)No payment required at authorization![A screenshot of a webpage Apple Pay payment sheet for a fixed subscription that doesn’t require payment until after the first month. The total shows a zero dollar amount.](https://docs-assets.developer.apple.com/published/0f2803def669b2fba7d8eb12f0545053/no-payment-required-web@2x.png)No payment required at authorization**Clarify the current payment amount in the total line.** Make sure people know the amount they’re being billed at the time of authorization.

**Only show the payment sheet when a subscription change results in additional fees.** When the someone changes a subscription, authorization isn’t necessary if the cost decreases or remains the same.

### [Supporting donations](/design/human-interface-guidelines/apple-pay#Supporting-donations)

[Approved nonprofits](https://developer.apple.com/support/apple-pay-nonprofits/)
 can use Apple Pay to accept donations.

**Use a line item to denote a donation.** Display a line item on the payment sheet that reminds people they’re authorizing a donation; for example, display Donation $50.00.

**Streamline checkout by offering predefined donation amounts.** You can reduce steps in the donation process by offering one-step recommended donations, like $25, $50, $100. Be sure to include an Other Amount option too, so people can customize the donation if they prefer.

[Using Apple Pay buttons](/design/human-interface-guidelines/apple-pay#Using-Apple-Pay-buttons)
-----------------------------------------------------------------------------------------------

The system provides several Apple Pay button types and styles you can use in your app or website. In contrast to the Apple Pay buttons, you use the [Apple Pay mark](/design/human-interface-guidelines/apple-pay#Apple-Pay-mark)
 to communicate the availability of Apple Pay as a payment option.

Don’t create your own Apple Pay button design or attempt to mimic the system-provided button designs.

For developer guidance, see [`PKPaymentButtonType`](/documentation/passkit/pkpaymentbuttontype)
 and [`PKPaymentButtonStyle`](/documentation/passkit/pkpaymentbuttonstyle)
 (iOS and macOS), [`WKInterfacePaymentButton`](/documentation/watchkit/wkinterfacepaymentbutton)
 (watchOS), and [Apple Pay on the Web](/documentation/apple_pay_on_the_web)
 (web).

### [Button types](/design/human-interface-guidelines/apple-pay#Button-types)

Apple provides several types of buttons so you can choose the button type that fits best with the terminology and flow of your purchase or payment experience.

Use the Apple-provided APIs to create Apple Pay buttons. When you use the system-provided APIs, you get:

* A button that is guaranteed to use an Apple-approved caption, font, color, and style
* Assurance that the button’s contents maintain ideal proportions as you change its size
* Automatic translation of the button’s caption into the language that’s set for the device
* Support for configuring the button’s corner radius to match the style of your UI
* A system-provided alternative text label that lets VoiceOver describe the button



| Payment button type | Example usage |
| --- | --- |
| Buy with Apple Pay button | An area in an app or website where people can make a purchase, such as a product detail page or shopping cart page. |
| Pay with Apple Pay button | An app or website that lets people pay bills or invoices, such as those for a utility — like cable or electricity — or a service like plumbing or car repair. |
| Check out with Apple Pay button | An app or website offering a shopping cart or purchase experience that includes other payment buttons that start with the text *Check out*. |
| Continue with Apple Pay button | An app or website offering a shopping cart or purchase experience that includes other payment buttons that start with the text *Continue with*. |
| Book with Apple Pay button | An app or website that helps people book flights, trips, or other experiences. |
| Donate with Apple Pay button | An app or website for an [approved nonprofit](https://developer.apple.com/support/apple-pay-nonprofits/)
 that lets people make donations. |
| Subscribe with Apple Pay button | An app or website that lets people purchase a subscription, such as a gym membership or a meal-kit delivery service. |
| Reload with Apple Pay button | An app or website that uses the term *reload* to help people add money to a card, account, or payment system associated with a service, such as transit or a prepaid phone plan. |
| Add Money with Apple Pay button | An app or website that uses the term *add money* to help people add money to a card, account, or payment system associated with a service, such as transit or a prepaid phone plan. |
| Top Up with Apple Pay button | An app or website that uses the term *top up* to help people add money to a card, account, or payment system associated with a service, such as transit or a prepaid phone plan. |
| Order with Apple Pay button | An app or website that lets people place orders for items like meals or flowers. |
| Rent with Apple Pay button | An app or website that lets people rent items like cars or scooters. |
| Support with Apple Pay button | An app or website that uses the term *support* to help people give money to projects, causes, organizations, and other entities. |
| Contribute with Apple Pay button | An app or website that uses the term *contribute* to help people give money to projects, causes, organizations, and other entities. |
| Tip with Apple Pay button | An app or website that lets people tip for goods or services. |
| Apple Pay button | An app or website that has stylistic reasons to use a button that can have a smaller minimum width or that doesn’t specify a call to action. If you choose a payment button type that isn’t supported on the version of the operating system your app or website is running in, the system may replace it with this button. |

When a device supports Apple Pay, but it hasn’t been set up yet, you can use the Set up Apple Pay button to show that Apple Pay is accepted and to give people an explicit opportunity to set it up.

![Set up Apple Pay button](https://docs-assets.developer.apple.com/published/6cd4e0f51f10a280e70eb9cc2325d1d1/button-set-up@2x.png)

You can display the Set up Apple Pay button on pages such as a Settings page, a user profile screen, or an interstitial page. Tapping the button in any of these locations needs to initiate the process of adding a card.

### [Button styles](/design/human-interface-guidelines/apple-pay#Button-styles)

You can use the *automatic* style to let the current system appearance determine the appearance of the Apple Pay buttons in your app (for developer guidance, see [`PKPaymentButtonStyle.automatic`](/documentation/passkit/pkpaymentbuttonstyle/automatic)
). If you want to control the button appearance yourself, you can use one of the following options. For web developer guidance, see [`ApplePayButtonStyle`](/documentation/apple_pay_on_the_web/applepaybuttonstyle)
.

#### [Black](/design/human-interface-guidelines/apple-pay#Black)

Use on white or light-color backgrounds that provide sufficient contrast. Don’t use on black or dark backgrounds.

![An illustration showing the correct placement of a black Apple Pay button over a light background.](https://docs-assets.developer.apple.com/published/a43fe0ccf43a3a34f043949225b6c4d5/apple-pay-black-yes@2x.png)

![Correct usage](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark@2x.png)

![An illustration showing the incorrect placement of a black Apple Pay button over a dark background.](https://docs-assets.developer.apple.com/published/ef1773a19ca65487a65f75bb99496c40/apple-pay-black-no@2x.png)

![Incorrect usage](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout@2x.png)

#### [White with outline](/design/human-interface-guidelines/apple-pay#White-with-outline)

Use on white or light-color backgrounds that don’t provide sufficient contrast. Don’t place on dark or saturated backgrounds.

![An illustration showing the correct placement of a white, outlined Apple Pay button over a light background.](https://docs-assets.developer.apple.com/published/3ae557e25ef4b90277cd75d448fef392/apple-pay-outline-yes@2x.png)

![Correct usage](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark@2x.png)

![An illustration showing the incorrect placement of a white, outlined Apple Pay button over a dark background.](https://docs-assets.developer.apple.com/published/0f49f420cd2712bd8a285c56ce7dee2f/apple-pay-outline-no@2x.png)

![Incorrect usage](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout@2x.png)

#### [White](/design/human-interface-guidelines/apple-pay#White)

Use on dark-color backgrounds that provide sufficient contrast.

![An illustration showing the correct placement of a white Apple Pay button over a dark background.](https://docs-assets.developer.apple.com/published/8e5e6f393b1c53f2e6e3a778663d0236/apple-pay-white-yes@2x.png)

![Correct usage](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark@2x.png)

![An illustration showing the incorrect placement of a white Apple Pay button over a light background.](https://docs-assets.developer.apple.com/published/d0cf8a7d077fcc20e2cc86ebd5e8261e/apple-pay-white-no@2x.png)

![Incorrect usage](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout@2x.png)

### [Button size and position](/design/human-interface-guidelines/apple-pay#Button-size-and-position)

**Prominently display the Apple Pay button.** Make the Apple Pay button no smaller than other payment buttons, and avoid making people scroll to see it.

![An illustration showing an Apple Pay button positioned correctly above a custom Add to Cart button. Both buttons are the same size.](https://docs-assets.developer.apple.com/published/b201eefa5937df07aa4fcff10cf3ac36/ap-same-size-correct@2x.png)

![Correct usage](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark@2x.png)

![An illustration showing an Apple Pay button positioned incorrectly at a smaller size above a larger custom Add to Cart button.](https://docs-assets.developer.apple.com/published/53a56e2127330516c38ffda8308e7f82/ap-smaller-incorrect@2x.png)

![Incorrect usage](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout@2x.png)

**Position the Apple Pay button correctly in relation to an Add to Cart button.** In a side-by-side layout, place the Apple Pay button to the right of an Add to Cart button.

![An illustration showing a Check Out with Apple Pay button correctly positioned to the right of a custom Add to Cart button.](https://docs-assets.developer.apple.com/published/3d08f86fef8bbf8ef8d0bb30e95911e0/ap-right-side-correct@2x.png)

![Correct usage](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark@2x.png)

![An illustration showing a Check Out with Apple Pay button incorrectly positioned to the left of a custom Add to Cart button.](https://docs-assets.developer.apple.com/published/f2b08052e5161c66959816ab2949e4b5/ap-left-side-incorrect@2x.png)

![Incorrect usage](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout@2x.png)

In a stacked layout, place the Apple Pay button above an Add to Cart button.

![An illustration of a Check Out with Apple Pay button correctly positioned above a custom Add to Cart button.](https://docs-assets.developer.apple.com/published/b201eefa5937df07aa4fcff10cf3ac36/ap-top-correct@2x.png)

![Correct usage](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark@2x.png)

![An illustration of a Check Out with Apple Pay button incorrectly positioned below a custom Add to Cart button.](https://docs-assets.developer.apple.com/published/2cd6a51f04852337fc16dacb58198851/ap-below-incorrect@2x.png)

![Incorrect usage](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout@2x.png)

**Adjust the corner radius to match the appearance of other buttons.** By default, an Apple Pay button has rounded corners. You can change the corner radius to produce a button with square corners or a pill-shaped button. For developer guidance, see [`cornerRadius`](/documentation/passkit/pkpaymentbutton/2999416-cornerradius)
.

![An illustration showing a Check Out with Apple Pay button above a custom Add to Cart button. Both buttons have 90-degree corners.](https://docs-assets.developer.apple.com/published/d910506f4d9d613db7d6c977fcba8fbd/minimum-corner-radii@2x.png)Minimum corner radius![An illustration showing a Check Out with Apple Pay button above a custom Add to Cart button. Both buttons have the default corner radius.](https://docs-assets.developer.apple.com/published/3788cd425c4fac8526a8888bc08bfedf/default-corner-radii@2x.png)Default corner radius![An illustration showing a Check Out with Apple Pay button above a custom Add to Cart button. Both buttons have the maximum corner radius, which results in a lozenge-like appearance.](https://docs-assets.developer.apple.com/published/bc7e5ae216657c5583c15aeeed5e5938/maximum-corner-radii@2x.png)Maximum corner radius**Maintain the minimum button size and margins around the button.** Be mindful that the button title may vary in length depending on the locale.

Note

If the size you specify doesn’t accommodate the translated title for the type of payment button you’re using, the system automatically replaces it with the plain Apple Pay button shown below on the left. There is no automatic replacement for the Set up Apple Pay button.

![An illustration of an Apple Pay button, labeled to indicate minimum margins of one-tenth the button’s height, a 100-point minimum width, and a 30-point minimum height.](https://docs-assets.developer.apple.com/published/b87d2cdec70ad67f8b095e47d7585ef5/minimum-apple-pay@2x.png)

![An illustration of a Donate with Apple Pay button, labeled to indicate minimum margins of one-tenth the button’s height, a 140-point minimum width, and a 30-point minimum height.](https://docs-assets.developer.apple.com/published/e7aede97d7f6acfd2f5b097ce5850168/minimum-apple-pay-donate@2x.png)

Use the following values for guidance.



| Button | Minimum width | Minimum height | Minimum margins |
| --- | --- | --- | --- |
| Apple Pay | 100pt (100px @1x, 200px @2x) | 30pt (30px @1x, 60px @2x) | 1/10 of the button’s height |
| Book with Apple Pay | 140pt (140px @1x, 280px @2x) | 30pt (30px @1x, 60px @2x) | 1/10 of the button’s height |
| Buy with Apple Pay |
| Check out with Apple Pay |
| Donate with Apple Pay |
| Set up Apple Pay |
| Subscribe with Apple Pay |

### [Apple Pay mark](/design/human-interface-guidelines/apple-pay#Apple-Pay-mark)

Use the Apple Pay mark graphic to show that Apple Pay is an available payment option when showing other payment options in a similar manner. The Apple Pay mark isn’t a button; if you need an Apple Pay button, choose one of the buttons described in [Button types](/design/human-interface-guidelines/apple-pay#Button-types)
. For design guidance related to showing Apple Pay as a payment option, see [Offering Apple Pay](/design/human-interface-guidelines/apple-pay#Offering-Apple-Pay)
.

![A row of four credit card logos, all of which are the same size and shape. The leftmost logo is the Apple Pay mark.](https://docs-assets.developer.apple.com/published/eb623bea0d2c8176ba590efef4493b9d/apple-pay-mark-with-payment-options@2x.png)

**Use only the artwork provided by Apple, with no alterations other than height.** You can specify a height for the Apple Pay mark, but make sure that the height you use is equal to or larger than other payment brand marks in your payment flow. Don’t adjust the width, corner radius, or aspect ratio of the artwork; don’t add a trademark symbol or any other content; don’t remove the border; don’t add visual effects to the mark, such as shadows, glows, or reflections; and don’t flip, rotate, or animate the Apple Pay mark.

**Maintain a minimum clear space around the mark of 1/10 of its height.** Don’t let the Apple Pay mark share its surrounding border with another graphic or button.

Download the Apple Pay mark graphic and full usage guidelines [here](/apple-pay/marketing/)
.

[Referring to Apple Pay](/design/human-interface-guidelines/apple-pay#Referring-to-Apple-Pay)
---------------------------------------------------------------------------------------------

As with all Apple product names, use Apple Pay exactly as shown in [Apple Trademark List](https://www.apple.com/legal/intellectual-property/trademark/appletmlist.html)
 — never make it plural or possessive — and adhere to [Guidelines for Using Apple Trademarks](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html)
.

You can use plain text to promote Apple Pay and indicate that Apple Pay is a payment option.

**Capitalize Apple Pay in text as it appears in the Apple Trademark list.** Use two words with an uppercase *A*, an uppercase *P*, and lowercase for all other letters. Display Apple Pay entirely in uppercase only when doing so is necessary for conforming to an established, typographic interface style, such as in an app that capitalizes all text.

**Never use the Apple logo to represent the name *Apple* in text.** In the United States, use the registered trademark symbol (®) the first time Apple Pay appears in body text. Don’t include a registered trademark symbol when Apple Pay appears as a selection option during checkout.



|  | Example text |
| --- | --- |
| Correct usage | Purchase with Apple Pay |
| Correct usage | Purchase with Apple Pay® |
| Incorrect usage | Purchase with ApplePay |
| Incorrect usage | Purchase with  Pay |
| Incorrect usage | Purchase with APPLE PAY |

**Coordinate the font face and size with your app.** Don’t mimic Apple typography. Instead, use text attributes that are consistent with the rest of your app or website.

**Don’t translate *Apple Pay* or any other Apple trademark.** Always use Apple trademarks in English, even when they appear within non-English text.

**In a payment selection context, you can display a text-only description of Apple Pay only when all payment options have text-only descriptions.** If any other payment option description includes an icon or logo, you must use the Apple Pay mark as described in [Offering Apple Pay](/design/human-interface-guidelines/apple-pay#Offering-Apple-Pay)
.

**When promoting your app’s use of Apple Pay, follow App Store guidelines.** Before promoting Apple Pay for your app, refer to the [App Store marketing guidelines](https://developer.apple.com/app-store/marketing/guidelines/)
.

[Platform considerations](/design/human-interface-guidelines/apple-pay#Platform-considerations)
-----------------------------------------------------------------------------------------------

*No additional considerations for iOS, iPadOS, macOS, visionOS, or watchOS. Not supported in tvOS.*

[Resources](/design/human-interface-guidelines/apple-pay#Resources)
-------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/apple-pay#Related)

[Apple Pay Marketing Guidelines](https://developer.apple.com/apple-pay/marketing/)


#### [Developer documentation](/design/human-interface-guidelines/apple-pay#Developer-documentation)

[Apple Pay](/documentation/passkit/apple_pay)


[Apple Pay on the Web](/documentation/apple_pay_on_the_web)


[`WKInterfacePaymentButton`](/documentation/watchkit/wkinterfacepaymentbutton)


#### [Videos](/design/human-interface-guidelines/apple-pay#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/119/8807F4D5-2547-422A-90F9-E7AD6C80004C/4987_wide_250x141_1x.jpg) What's new in Wallet and Apple Pay](https://developer.apple.com/videos/play/wwdc2021/10092) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/49/19E76490-5848-40B3-A597-FE0D384144AC/3401_wide_250x141_1x.jpg) What's new in Wallet and Apple Pay](https://developer.apple.com/videos/play/wwdc2020/10662) 
[Change log](/design/human-interface-guidelines/apple-pay#Change-log)
---------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| May 2, 2023 | Consolidated guidance into one page. |

