# **[technologies-apple-pay] subscriptions-and-donations**

If you offer subscriptions or support other types of recurring payments, or if you’re a non-profit that accepts donations, follow these guidelines.

# **Subscriptions**

Your app or website can use Apple Pay to request authorization for recurring fees. A recurring fee can be a fixed amount, such as a monthly movie ticket subscription, or — when local regulations allow — a variable amount like a weekly grocery order. The initial authorization can also include discounts and additional fees.

---

### • [iOS](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/subscriptions-and-donations#)

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePaySheet-fixedsubscription_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePaySheet-fixedsubscription_2x.png)

Fixed subscription

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePaySheet-variablesubscription_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePaySheet-variablesubscription_2x.png)

Variable subscription (where local regulations allow)

### • [Web](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/subscriptions-and-donations#)

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/webpay-fixed_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/webpay-fixed_2x.png)

Fixed subscription

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/webpay-variable_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/webpay-variable_2x.png)

Variable subscription (where local regulations allow)

---

**Clarify subscription details before showing the payment sheet.** Before asking people to authorize a recurring payment, make sure they fully understand the billing frequency and any other terms of service. You can reiterate the billing frequency on the payment sheet.

**Include line items that reiterate billing frequency, discounts, and additional upfront fees.**Use these line items to remind people what they’re authorizing. If no payment is required at authorization time, clearly disclose when billing will occur.

---

### • [iOS](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/subscriptions-and-donations#)

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePaySheet-no-payment-required_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePaySheet-no-payment-required_2x.png)

No payment required at authorization

### • [Web](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/subscriptions-and-donations#)

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePay-Web-ZeroPayment_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePay-Web-ZeroPayment_2x.png)

No payment required at authorization

---

**Clarify the current payment amount in the total line.** Make sure people know the amount they’re being billed at the time of authorization.

**Only show the payment sheet when a subscription change results in additional fees.** When the someone changes a subscription, authorization isn’t necessary if the cost decreases or remains the same.

# **Donations**

[Approved nonprofits](https://developer.apple.com/support/apple-pay-nonprofits/) can use Apple Pay to accept donations.

**Use a line item to denote a donation.** Display a line item on the payment sheet that reminds people they’re authorizing a donation; for example, display Donation $50.00.

**Streamline checkout by offering predefined donation amounts.** You can reduce steps in the donation process by offering one-step recommended donations, like $25, $50, $100. Be sure to include an Other Amount option too, so people can customize the donation if they prefer.