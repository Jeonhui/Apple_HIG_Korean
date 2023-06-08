# **[technologies] wallet**

# Wallet helps people securely store their credit and debit cards, driver’s license or state ID, transit cards, event tickets, keys, and more on iPhone and Apple Watch.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-Wallet-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-Wallet-intro_2x.png)

People use their cards and passes in Wallet to make Apple Pay — and Apple Pay Later — purchases, track their orders, confirm their identity, and streamline activities like boarding a plane, attending a concert, or receiving a discount.

When you integrate Apple Wallet into your app, you can create custom passes and present them the moment people need them, securely verify an individual’s identity so they can access personal content, and offer detailed receipts and tracking information where it’s most convenient. For developer guidance, see [Wallet](https://developer.apple.com/documentation/passkit/wallet).

# **Passes**

**Offer to add new passes to Wallet.** When people do something that results in a new pass — like checking into a flight, purchasing an event ticket, or registering for a store reward program — you can present system-provided UI that helps them add the pass to Wallet with one tap (for developer guidance, see [addPasses(_:withCompletionHandler:)](https://developer.apple.com/documentation/passkit/pkpasslibrary/1617093-addpasses)). If people want to review a pass before adding it, you can display a custom view that displays the pass and provides an Add to Apple Wallet button; for developer guidance, see [PKAddPassesViewController](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller).

**Help people add a pass that they created outside of your app.** If people create a pass using your website or another device, suggest adding it to Wallet the next time they open your app. If people decline your suggestion, don’t ask them again.

**Add related passes as a group.** If your app generates multiple passes, like boarding passes for a multi-connection flight, add all passes at the same time so people don’t have to add each one individually. If people can receive a group of passes from your website — such as a set of tickets for an event — bundle them together so that people can download all of them at one time. For developer guidance, see [Distributing and updating a pass](https://developer.apple.com/documentation/walletpasses/distributing_and_updating_a_pass).

**Display an Add to Apple Wallet button to let people add an existing pass that isn’t already in Wallet.** If people previously declined your suggestion to add a pass to Wallet — or if they removed the pass — a button makes it easy to add it if they change their minds. You can display an Add to Apple Wallet button wherever the corresponding pass information appears in your app. For developer guidance, see [PKAddPassButton](https://developer.apple.com/documentation/passkit/pkaddpassbutton). You can also display an Add to Apple Wallet badge in an email or on a webpage; for guidance, see [Add to Apple Wallet guidelines](https://developer.apple.com/wallet/add-to-apple-wallet-guidelines/).

**Let people jump from your app to their pass in Wallet.** Wherever your app displays information about a pass that exists in Wallet, you can offer a link that opens it directly. Label the link something like “View in Wallet.”

**Consider hiding expired passes.** In iOS 15 and later, Wallet automatically hides expired passes to reduce crowding, while also providing a button that lets people revisit them. To ensure the system hides passes appropriately, set the expiration date, relevant date, and voided properties of each pass correctly; for developer guidance, see [Pass](https://developer.apple.com/documentation/walletpasses/pass/).

**Always get people’s permission before deleting a pass from Wallet.** For example, you could include an in-app setting that lets people specify whether they want to delete passes manually or have them removed automatically. If necessary, you can display an alert before deleting a pass.

**Help the system suggest a pass on the Lock Screen when it’s contextually relevant.** Ideally, passes automatically appear when they’re needed so people don’t have to manually locate them. When you supply information about when and where your pass is relevant, the system can display a link to it on the Lock Screen when people are most likely to want it. For example, a gym membership card could appear on the Lock Screen as people enter the gym. For developer guidance, see [Showing a pass on the Lock Screen](https://developer.apple.com/documentation/walletpasses/pass/showing_a_pass_on_the_lock_screen/).

![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/screen-notification_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/screen-notification_2x.png)

**Update passes as needed.** Physical passes don’t typically change, but a digital pass should reflect updates to events. An airline boarding pass, for example, should automatically update to display flight delays and gate changes.

**Use change messages only for updates to time-critical information.** A change message interrupts the user’s current workflow, so it’s essential to send one only when you make an update that people must know about. For example, people need to know when there’s a gate change in a boarding pass, but they don’t need to know when a customer service phone number changes. Never use a change message for marketing or other noncritical communication. You enable change messages on a per-field basis; for developer guidance, see [Adding a web service to update passes](https://developer.apple.com/documentation/walletpasses/adding_a_web_service_to_update_passes/).

# **Designing passes**

Wallet uses a consistent design aesthetic to strengthen familiarity and build trust. Instead of merely replicating the appearance of a physical item, design a clean, simple pass that looks at home in Wallet.

![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/pass-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/pass-intro_2x.png)

**Design a pass that looks great and works well on all devices.** Passes can look different on different devices. For example, when a pass appears on Apple Watch, it doesn’t display all the images it displays when it appears on iPhone (for guidance, see [Passes for Apple Watch](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet#passes-for-apple-watch)). Don’t put essential information in elements that might be unavailable on certain devices. Also, don’t add padding to images; for example, watchOS crops white space from some images.

**Avoid using device-specific language.** You can’t predict the device people will use to view your pass, so don’t include copy that might not make sense on a particular device. For example, copy that tells people to “slide to view” content doesn’t make sense when it appears on Apple Watch.

**Make your pass instantly identifiable.** Using color — especially a color that’s linked to your brand — can help people recognize your pass as soon as they see it. Make sure that pass content remains comfortably readable against the background you choose.

**Keep the front of a pass uncluttered so people can get important information at a glance.**Show essential information — like an event date or account balance — in the top-right area of the pass so people can still see it when the pass is collapsed in Wallet. Use the rest of the pass front to provide important information; consider putting extra information on the back of a pass (iOS) or in a details screen (watchOS).

**Prefer an NFC-enabled pass.** People appreciate having a contactless pass, because it means that they can just hold their device near a reader. If you support both NFC and a barcode or QR code, the code appears on the back of the pass (in iOS) or in the details screen (in watchOS). In iOS, you can display a QR code or barcode on the front of your pass if necessary for your design.

**Reduce image sizes for optimal performance.** People can receive passes via email or a webpage. To make downloads as fast as possible, use the smallest image files that still look great.

**Provide an icon that represents your company or brand.** The system includes your icon when displaying information about a relevant pass on the lock screen. Mail also uses the icon to represent your pass in an email message. You can use your app icon or design an icon for this purpose. Create an icon that measures a minimum of 38x38 pts.

The system defines several pass *styles*, each of which specifies the overall appearance of a pass in categories like event ticket, boarding pass, and coupon. The pass style determines the layout of your content, and can affect the types of relevancy information you provide (for guidance, see [Passes](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet#passes)).

Although each pass style is different, all styles display information using the basic layout areas shown below:

![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/pass-layout-diagram_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/pass-layout-diagram_2x.png)

All passes display a logo image; depending on style, passes can display additional images in other areas. To display text, you use the following [pass fields](https://developer.apple.com/documentation/walletpasses/passfields) to provide content within specific layout areas:

| Field | Layout area | Use to provide... |
| --- | --- | --- |
| Header | Essential | Critical information that should remain visible when the pass is collapsed in Wallet. |
| Primary | Primary | Important information that helps people use the pass. |
| Secondary and auxiliary | Secondary and auxiliary | Useful information that people might not need every time they use the pass. |
| Back | Not shown in diagram | Supplemental details that don’t need to be on the pass front. |

In general, a pass can have up to three header fields, one primary field, up to four secondary fields, and up to four auxiliary fields. Depending on the amount of content you display in each field, some fields may not be visible.

**Display text only in pass fields.** The system ensures that text in pass fields is legible and accessible to assistive technologies like VoiceOver. Don’t embed text in images — it’s not accessible and not all images are displayed on all devices — and avoid using custom fonts that might make text hard to read.

# **Boarding passes**

Use the boarding pass style for train tickets, airline boarding passes, and other types of transit passes. Typically, each pass corresponds to a single trip with a specific starting and ending point.

A boarding pass can display logo and footer images, and it can have up to two primary fields and up to five auxiliary fields.

• [Example](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet#)
• [Layout](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet#)

-

![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/boarding_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/boarding_2x.png)


# **Coupons**

Use the coupon style for coupons, special offers, and other discounts. A coupon can display logo and strip images, and it can have up to four secondary and auxiliary fields, all displayed on one row.

• [Example](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet#)
• [Layout](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet#)

-

![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/coupon_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/coupon_2x.png)


# **Store cards**

Use the store card style for store loyalty cards, discount cards, points cards, and gift cards. If an account related to a store card carries a balance, the pass usually shows the current balance.

A store card can display logo and strip images, and it can have up to four secondary and auxiliary fields, all displayed on one row.

• [Example](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet#)
• [Layout](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet#)

-

![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/store-card_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/store-card_2x.png)


# **Event tickets**

Use the event ticket style to give people entry into events like concerts, movies, plays, and sporting events. Typically, each pass corresponds to a specific event, but you can also use a single pass for several events, as with a season ticket.

An event ticket can display logo, strip, background, or thumbnail images. However, if you supply a strip image, don’t include a background or thumbnail image. You can also include an extra row of up to four auxiliary fields (for developer guidance, see the `row` property of [PassFields.AuxiliaryFields](https://developer.apple.com/documentation/walletpasses/passfields/auxiliaryfields)).

• [Example](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet#)
• [Layout](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet#)

-

![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/event-ticket_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/event-ticket_2x.png)


# **Generic passes**

Use the generic style for a type of pass that doesn’t fit into the other categories, such as a gym membership card or coat-check claim ticket. A generic pass can display logo and thumbnail images, and it can have up to four secondary and auxiliary fields, all displayed on one row.

• [Example](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet#)
• [Layout](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet#)

-

![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/generic_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/generic_2x.png)


# **Passes for Apple Watch**

On Apple Watch, Wallet displays passes in a scrolling carousel of cards. People can add your pass to their Apple Watch even if you don’t create a watch-specific app, so it’s important to understand how your pass can look on the device.

![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/watch-pass-design-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/watch-pass-design-intro_2x.png)

On their Apple Watch, people can tap a card to reveal a details screen that displays additional pass information in a scrolling view. In some cases, people can also tap a specific transaction to get more information.

![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/watch-card-and-details_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/watch-card-and-details_2x.png)

Each pass style specifies the fields and images that can appear in the basic layout areas shown below:

![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/watch-layout-diagram_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/watch-layout-diagram_2x.png)

If some information doesn’t fit within the layout areas, the system displays it in the scrolling details screen.

**IMPORTANT**In every style, watchOS crops the strip image to fit the aspect ratio of the card interface and may crop white space from other images.

• [Boarding](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet#)
• [Coupon](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet#)
• [Store](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet#)
• [Event](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet#)
• [Generic](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet#)

-

![https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/watch-layout-boarding-pass_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet/images/watch-layout-boarding-pass_2x.png)


# **Order tracking**

When you support Order Tracking, Wallet can automatically display information about an order after people successfully complete an Apple Pay purchase through your app or website, updating the information whenever the status of the order changes.

Wallet presents a dashboard that displays a customer’s active and completed orders. People can choose an order to view details about it, like the items they ordered and fulfillment information for shipping and pickup.

The [Wallet Orders](https://developer.apple.com/documentation/walletorders) schema defines the fields you use to provide order data like product descriptions, order status, contact information, and shipping and pickup details, including estimated arrival dates, addresses, tracking numbers, and pickup instructions. Wallet displays the information you supply within consistent, system-defined interfaces. To help people get the information they need quickly and conveniently, supply as much information as you can, using the fields that match your order processes.

**Make data available immediately after people place an order.** People often want to confirm that their order was received, even when payment, processing, and fulfillment are still pending. It’s essential to provide existing information quickly so that the system can display it right away.

**Provide fulfillment information as soon as it’s available, and keep the status up to date.**When you supply fulfillment data or you change the status of an order, the system updates the order information and can automatically send a notification to customers. The system uses the fulfillment status you report to update the order’s current status to a value like Order Placed, Processing, Ready for Pickup, Picked Up, Out for Delivery, Delivered, or — if something goes wrong — Issue or Canceled. For guidance on describing a status, see [Displaying order and fulfillment details](https://developer.apple.com/design/human-interface-guidelines/technologies/wallet#displaying-order-and-fulfillment-details).

**Supply a high-resolution logo image.** The system displays your logo image in the dashboard and detail view, so you want to make sure that people can instantly recognize it at various sizes. Use the PNG or JPEG format to create a logo image that measures 300x300 pixels. For developer guidance, see [logo](https://developer.apple.com/documentation/walletorders/merchant).

**Supply distinct, high-resolution product images.** The system displays a product’s image — along with descriptive information you supply — in the detail views, order dashboard, and notifications for an order or a fulfillment. When creating a product image, prefer using a straightforward depiction and a solid background. Showing a product in a “lifestyle” context or against a busy background can make the item hard to distinguish at small sizes. For each product, use the PNG or JPEG format to create an image that measures 300x300 pixels.

**In general, keep text brief.** People appreciate being able to read text at a glance, and the system can truncate text that’s too long.

**Use clear, approachable language, and localize the text you provide.** You want to make sure that all your customers can read the information in an order. Also, make sure the price you show matches the final price the customer confirmed.

# **Displaying order and fulfillment details**

An order gives people ways to contact you and displays details about their Apple Pay purchase, including fulfillment status and per-item information.

**Provide a link to an area where people manage their order.** When you provide a universal link, people can open your order management area even if they don’t have your app installed. To learn more about universal links, see [Allowing apps and websites to link to your content](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content?preferredLanguage=occ); for developer guidance, see [orderManagementURL](https://developer.apple.com/documentation/walletorders/order).

**Clearly describe each item so people can verify that their order contains everything they expect.** You can use the [lineItem](https://developer.apple.com/documentation/walletorders/lineitem) field to provide information like a product’s price, name, and image. An order lists the line items for every item the customer ordered; a fulfillment lists only the line items that fulfillment includes.

**Supply a prioritized list of your apps that might be installed on the device.** The system uses this list when it needs to display a link to your app within the order details view. For example, if you provide multiple apps and more than one of them is installed on the device, the system displays a link to the installed app that’s highest on your list. If none of your apps are installed on the device, the system displays a link to the first app on your list. For developer guidance, see [associatedApplications](https://developer.apple.com/documentation/walletorders/order).

**Avoid sending duplicate notifications.** For example, you can tell the system to avoid sending order-related notifications through Wallet when the customer has one of your associated apps installed.

**Make it easy for customers to contact you.** Provide multiple contact methods, so people can choose the one that works best for them. At minimum, you need to provide a link to your website or landing page, but you can also provide a Messages for Business link, a phone number, an email address, and a link to your support page (for developer guidance, see [Merchant](https://developer.apple.com/documentation/walletorders/merchant)). When people choose the Contact button in an order, the system displays a menu of the contact methods you supply.

**Help people track their order.** A multi-item order can have multiple fulfillments, where each fulfillment is either shipping or pickup. For example, if a customer orders a pair of shoes and a T-shirt, the customer might want to have one item shipped, while picking up the other. Regardless of fulfillment type, you need to supply enough information for people to know where their items are and when to expect them at the destination they specified. In addition to an estimated time of arrival, here’s some information that people particularly appreciate:

- A link that opens the carrier’s website to a page with information about a shipping fulfillment. When possible, provide a direct link — in addition to a tracking number — so people can easily view the most up-to-date shipping information.
- A scannable barcode when one is required to pick up the order in a pickup fulfillment. It’s convenient when people can offer the barcode from within Wallet instead of finding it in an email or webpage.
- Clear, detailed instructions that can help people receive or pick up their order.

**Choose shipping-fulfillment values that match the details you have about the shipping process.** If you know the carrier, enter its name in the `carrier` field; otherwise, leave the default “Track Shipment” value. If you can access details about a carrier’s interim shipping steps — such as when a fulfillment is on the way or out for delivery — indicate each step by using specific status values like `onTheWay`, `outForDelivery`, or `delivered`. In contrast, if you don’t have access to a carrier’s shipping details, use the `shipped` status. In both cases, provide a tracking link (when one is available) so people can track their order on their own. For developer guidance, see [ShippingFulfillment](https://developer.apple.com/documentation/walletorders/shippingfulfillment).

**Keep customers informed through relevant fulfillment status descriptions.** A great status message is approachable, accurate, and clearly related to the status it describes. In addition to supplying information that helps people understand the status of their order, a status message also gives you an opportunity to use your brand’s communication style.

**Be direct and thorough when describing an Issue or Canceled status.** People generally need to know why there’s a problem and what they can do about it.

# **Identity verification**

On iPhone running iOS 16 and later, people can store an ID card in Wallet, and later allow an app or App Clip to access information on the card to verify their identity without leaving their current context. For example, a person might need to confirm their identity when they apply for a credit card within their banking app.

**DEVELOPER NOTE**Apple doesn’t create or see the ID documents that people add to Wallet, and when people agree to share identifying information with your app, you receive only encrypted data that isn’t readable on the device. For developer guidance, see [Requesting identity data from a Wallet pass](https://developer.apple.com/documentation/passkit/wallet/requesting_identity_data_from_a_wallet_pass).

To help you offer a consistent experience that people can trust, Apple provides a Verify with Wallet button you can use in your app when you need to ask for identify verification. The button reveals a sheet that describes your request and lets people agree to share their information or cancel.

**Present a Wallet verification option only when the device supports it.** If the current device can’t return the identify information you request, don’t display a Verify with Apple Wallet button. Be prepared to present a fallback view that offers a different verification method if Verify with Apple Wallet isn’t available; for developer guidance, see [VerifyIdentityWithWalletButton](https://developer.apple.com/documentation/passkit/verifyidentitywithwalletbutton).

**Ask for identity information only at the precise moment you need it.** People can be suspicious of a request for personal information if it doesn’t seem to be related to their current action. If your app needs identity verification, for example, wait to ask for this information until people are completing the process or transaction that requires it; don't request verification before people are ready to start the process or when they're simply creating an account.

**Clearly and succinctly describe the reason you need the information you’re requesting.** You must write copy (called a *purpose string* or *usage description string*) that explains why people need to share identity information with your app. The system displays your purpose string in the verification sheet so people can make an informed decision. Here are a couple of examples:

| To verify... | To support... | Example purpose string |
| --- | --- | --- |
| Identity | Opening an account for which proof of identity is legally required to prevent fraud | Federal law requires this information to verify your identity and also to help [App Name] prevent fraud. |
| Driving privilege | Renting a vehicle that requires legal driving privileges | Applicable state law requires [App Name] to verify your driving privileges. |

For each purpose string, aim for a brief, complete sentence that’s direct, specific, and easy for everyone to understand. Use sentence case, avoid passive voice, and include a period at the end.

**Ask only for the data you actually need.** People may lose trust in your app if you ask for more data than you need to complete the current task or action. For example, if you need to ensure that a customer is at least a certain age, use a request that specifies an age threshold; avoid requesting the customer’s current age or birth date. For developer guidance, see [age(atLeast:)](https://developer.apple.com/documentation/passkit/pkidentityelement/3930277-age).

**Clearly indicate whether you will keep the data and — if you need to keep it — specify how long you’ll do so.** To help people trust your app, it’s essential to explain how long you might need to keep the personal information they agree to share with you. When you use PassKit APIs to specify a duration — such as a particular period, indefinitely, or only as long as it takes to complete the current verification — the system automatically displays explanatory content in the verification sheet. For developer guidance, see [PKIdentityIntentToStore](https://developer.apple.com/documentation/passkit/pkidentityintenttostore).

**Choose the system-provided verification button that matches your use case and the visual design of your app.** The system provides the following button labels to support various use cases:

[제목 없음](https://www.notion.so/18138785e3b64f23862b051c2f16d51d)

All button labels are also available in a multiline variant that the system automatically uses when horizontal space is constrained. For developer guidance, see [PKIdentityButton.Label](https://developer.apple.com/documentation/passkit/pkidentitybutton/label).

The verification button always uses white letters on a black background. You can choose the style that includes a light outline if you need to ensure that the button contrasts well with a dark background in your app (for developer guidance, see [PKIdentityButton.Style.blackOutline](https://developer.apple.com/documentation/passkit/pkidentitybutton/style/blackoutline)). In addition, you can use the [cornerRadius](https://developer.apple.com/documentation/passkit/pkidentitybutton/3967461-cornerradius) property to adjust the verification button’s corners to match other related buttons in your interface.