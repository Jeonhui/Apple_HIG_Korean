# **[technologies-apple-pay] checkout-and-payment**

People appreciate using Apple Pay to make purchases quickly and easily. You can enhance the purchase experience in your app or website by creating a streamlined checkout process and presenting a customized payment sheet that lets people promptly authorize payment and complete their transaction.

# **Streamline the checkout process**

**Provide a cohesive checkout experience.** It’s best when the entire checkout flow feels tightly integrated with your app or website. To strengthen people’s perception of integration, use your branding throughout the checkout experience and avoid opening different pages or windows. For website checkout flows in particular, opening new windows during the process can cause confusion and may even lead people to think they’ve been handed off to a different website.

**If Apple Pay is enabled, assume the person wants to use it.** Consider presenting the Apple Pay button as the first payment option, displaying it larger than other options, or using a line to visually separate it from other choices.

**Accelerate single-item purchases with Apple Pay buttons on product detail pages.** In addition to offering a shopping cart, consider putting Apple Pay buttons on product detail pages so people can purchase an individual item quickly. Purchases initiated in this way should be for an individual item only, and should exclude any items that already reside in the shopping cart. If the shopping cart contains an item purchased directly from a product detail page, remove the item from the cart after the purchase is complete.

**Accelerate multi-item purchases with express checkout.** Consider providing an express checkout feature that immediately displays the payment sheet, allowing people to purchase multiple items quickly using a single shipping method and destination. If you offer a coupon or promotional code, you can enhance the express checkout experience by letting people enter it on the payment sheet.

**Collect necessary information, like color and size options, before people reach the Apple Pay button.** When additional information is needed at checkout time — perhaps because the customer forgot to choose an option — gracefully point out the problem and help them correct it. Use highlighting or warning text to identify missing information, and automatically navigate to the problematic field so people can correct it quickly and complete their purchase.

**Collect optional information before checkout begins.** There’s no way to input optional data — like gift messages or delivery instructions — on the payment sheet, so collect this information ahead of time or even after the purchase is complete.

**Gather multiple shipping methods and destinations before showing the payment sheet.** The payment sheet lets people select a single shipping method and destination for an entire order. If your customers can choose different shipping methods and destinations for individual items in an order, collect those details before Apple Pay checkout begins, instead of on the payment sheet.

**For in-store pickup, help people choose a pickup location before displaying the payment sheet.** After a customer chooses the pickup location they want, use the read-only format to display the location’s address on the payment sheet. For developer guidance, see [Displaying a read-only pickup address](https://developer.apple.com/documentation/passkit/pkpaymentrequest/displaying_a_read-only_pickup_address).

**Prefer information from Apple Pay.** Assume that Apple Pay information is complete and up to date. Even if your app or website has existing contact, shipping, and payment information, consider fetching the latest from Apple Pay during checkout to reduce potential corrections.

**Avoid requiring account creation prior to purchase.** If you want people to register for an account, ask them to do so on the order confirmation page. Prepopulate as many registration fields as possible using information provided by the payment sheet during checkout.

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/paymentSheet-before-account_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/paymentSheet-before-account_2x.png)

**Report the result of the transaction so that people can view it in the payment sheet.** In failure cases, the payment sheet can display the errors that you provide, so people can take steps to fix the problem.

**Display an order confirmation or thank-you page.** After the payment sheet shows the result of the transaction, display an order confirmation page to thank people for their purchase, provide details about when the order will ship, and indicate how to check its status. Listing Apple Pay on the confirmation page isn’t necessary, but if you do, show it after the last four digits of the account used to process the transaction or as a separate note. For example: ”1234 (Apple Pay)” or ”Paid with Apple Pay.”

# **Customize the payment sheet**

**Only present and request essential information.** People may get confused or have privacy concerns if the payment sheet includes extraneous information. For example, it makes sense to see a contact email address but not a shipping address if the purchase is a gift card that will be delivered electronically. Showing or asking for a shipping address in this scenario may give the false impression that something will be physically delivered.

**Display the active coupon or promotional code, or give people a way to enter it.** For example, if people can enter a code before the payment sheet appears, displaying it on the sheet can reassure them that the code works as they expect. Alternatively, enabling code entry on the payment sheet can be particularly beneficial in an express checkout flow.

**Let people choose the shipping method in the payment sheet.** To the extent space permits, show a clear description, a cost, and, optionally, an estimated delivery or pickup date — or range of dates — for each available option. In iOS 15 and later, you can take advantage of the shipping method’s calendar and time-zone support to provide accurate delivery or pickup information, regardless of the customer’s current location. For developer guidance, see [PKDateComponentsRange](https://developer.apple.com/documentation/passkit/pkdatecomponentsrange).

**For in-store pickup, consider letting people choose a pickup window that works for them.**You can use the shipping method to supply a range of dates and times from which people can choose.

**Use line items to explain additional charges, discounts, pending costs, add-on donations, recurring, and future payments.** A line item includes a label and cost; a line item for a recurring payment can also include a frequency. Don’t use line items to show an itemized list of products that make up the purchase. For developer guidance, see [paymentSummaryItems](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619231-paymentsummaryitems); for guidance on donations, see [Donations](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/subscriptions-and-donations/#donations).

• [iOS](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/checkout-and-payment#)
• [Web](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/checkout-and-payment#)

-

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePaySheet-additionalcharges-2_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePaySheet-additionalcharges-2_2x.png)


**Keep line items short.** Make line items specific and easily understandable at a glance. Whenever possible, fit line items on a single line.

**Provide a business name after the word *Pay* on the same line as the total.** Use the same business name people will see when they look for the charge on their bank or credit card statement. This provides reassurance that payment is going to the right place. For example: Pay [Business_Name].

**If you’re not the end merchant, specify both your business name and the end merchant’s name in the payment sheet.** There are a few ways your app, App Clip, or website might help people make a purchase from an end merchant that’s unrelated to your company. For example, a marketplace app can help people make a purchase from an end merchant they might not recognize. Another example is an app that offers a self-checkout service people can use to pay for an item in an end merchant’s physical store without visiting the store’s checkout counter. In scenarios like these, people might not realize two businesses are involved in the transaction, so it’s essential to name both businesses and clarify their roles. When your app acts as an intermediary for an end merchant, clearly and succinctly describe the situation in the Pay line of the payment sheet, using something like Pay [End_Merchant_Business_Name (via Your_Business_Name)].

**Clearly disclose when additional costs may be incurred after payment authorization.** In some cases, the total cost may be unknown at checkout time. For example, the price of a car ride based on distance or time might change after checkout. Or, a customer might want to add a tip after a product has been delivered. In situations like these, and when local regulations allow, you can provide a clear explanation in the payment sheet and a subtotal marked as ”Amount Pending.” If you are preauthorizing a specific amount, be sure the payment sheet accurately reflects this information.

**Handle data entry and payment errors gracefully.** If an error occurs during checkout, help people resolve it quickly so they can complete their transaction. For related guidance, see [Data validation](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/handling-errors/#data-validation).

### **Displaying a website icon**

Many websites provide an icon that can be displayed with bookmarks, in URL fields, or on a device’s Home screen. Websites that support Apple Pay can display this icon in a summary view and in the payment sheet of the connected device that’s used to authorize payment. The icon provides visual reassurance that payment is going to the right place.

If your website supports Apple Pay, provide an icon in the following sizes for use in the summary view and the payment sheet:

| @2x | @3x |
| --- | --- |
| 60x60 pt (120x120 px @2x) | 60x60 pt (180px180 px @3x) |

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/webicon-payment_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/webicon-payment_2x.png)