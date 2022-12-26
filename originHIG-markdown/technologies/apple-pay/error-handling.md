# **[technologies-apple-pay] error-handling**

Provide clear, actionable guidance when problems occur during checkout or payment processing, so people can resolve problems quickly and complete their transaction.

# **Data validation**

Your app or website can respond to user input when the payment sheet appears, when people change certain field values on the payment sheet, and after they authenticate the transaction. Use these opportunities to check for data entry problems and to provide clear and consistent messaging.

### • [iOS](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/handling-errors#)

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePaySheet-error_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePaySheet-error_2x.png)

Payment sheet error messaging

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePaySheet-error2_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePaySheet-error2_2x.png)

Custom detail view error messaging

### • [Web](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/handling-errors#)

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePayShippingErrorA_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePayShippingErrorA_2x.png)

Payment sheet error messaging

![https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePayShippingErrorB_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/apple-pay/images/ApplePayShippingErrorB_2x.png)

Custom detail view error messaging


When data is invalid, system-provided error messaging calls attention to relevant fields on the payment sheet. People can choose a field to view additional details and resolve the problem. Provide customized error messages for the detail view that appears when people choose a problematic field.

For developer guidance, see [PKPaymentAuthorizationViewControllerDelegate](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate) (iOS, watchOS) and [Apple Pay on the web](https://developer.apple.com/documentation/apple_pay_on_the_web) (web).

**NOTE**For privacy reasons, your app or website has limited access to data until people attempt to authorize a transaction. Prior to authorization, only the card type and a redacted shipping address are accessible. It’s critical to display errors when authorization fails, but to the extent possible, your app should also attempt to validate available information and report problems before authorization.

**Avoid forcing compliance with your business logic.** Design a data validation process that’s intelligent enough to ignore irrelevant data and infer missing data whenever possible. For example, if your app requires a five-digit zip code but someone enters a Zip+4 code, ignore the additional digits rather than asking for a correction. Let people enter phone numbers in multiple formats — such as with and without dashes, and with and without a country code — without producing an error.

**Provide accurate status reporting to the system.** When a problem occurs, it’s essential that your app or website accurately indicate the type of problem so the system can show the most relevant error message on the payment sheet. This is done by accompanying your custom error message with the correct status code. For developer guidance, see [PKPaymentError](https://developer.apple.com/documentation/passkit/pkpaymenterror) (iOS, watchOS) and [Apple Pay status codes](https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/apple_pay_status_codes) (web).

**Succinctly and specifically describe the problem when data is invalid or incorrectly formatted.** Reference the relevant field and indicate exactly what’s expected. For example, if people enter an invalid zip code, instead of showing “Address is invalid”, show a specific message like “Zip code doesn’t match city”. If the shipping address is unserviceable, indicate why with a message like “Shipping not available for this state”. Use noun phrases with sentence-style capitalization and no ending punctuation. Aim to keep messages at 128 characters or fewer to avoid truncation.

# **Payment processing**

**Handle interruptions correctly.** A user-driven event like a cancellation or a system-driven event like a timeout could cause an interruption in the payment flow, resulting in the payment sheet being dismissed. When such an event occurs, you must cancel any in-progress payment. After the payment sheet dismisses, people can restart the process by choosing the Apple Pay button again. For developer guidance, see [PKPaymentAuthorizationViewControllerDelegate](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate) (iOS, watchOS) and [oncancel](https://developer.apple.com/documentation/apple_pay_on_the_web/applepaysession/1778029-oncancel) (web).