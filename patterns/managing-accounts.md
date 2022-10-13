# **[patterns] managing-accounts**

# When it doesn’t create an unnecessary barrier to your experience, an account can be a convenient way for people to access their content and track personal details.
> 계정이 사용자의 경험에 불필요한 장벽을 만들지 않을 때, 계정은 사람들이 자신의 콘텐츠에 액세스하고 개인 정보를 추적할 수 있는 편리한 방법이 될 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-managing-accounts-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-managing-accounts-intro-dark_2x.png)

Ask people to create an account only if your core functionality requires it; otherwise, let people enjoy your app or game without one. If you require an account, consider using [Sign in with Apple](../technologies/sign-in-with-apple/introduction) to give people a consistent sign-in experience they can trust and the convenience of not having to remember multiple accounts and authentication methods.
> 핵심 기능에 필요한 경우에만 계정을 만들도록 요청하고, 그렇지 않으면 앱이나 게임을 즐길 수 있도록 합니다. 계정이 필요한 경우 Apple에 로그인하여 신뢰할 수 있는 일관된 로그인 환경을 제공하고 여러 계정과 인증 방법을 기억하지 않아도 되는 편리함을 제공하는 것을 고려해 보십시오.
>




# **Best practices**

**Explain the benefits of creating an account and how to sign up.** If your app or game requires an account, write a brief, friendly description of the reasons for the requirement and its benefits. Display this message on the sign-in screen.
> 계정 생성의 이점과 가입 방법에 대해 설명합니다. 당신의 앱이나 게임에 계정이 필요하다면, 요구 사항의 이유와 그 이점에 대한 간단하고 친근한 설명을 쓰세요. 로그인 화면에 이 메시지를 표시합니다.
>




**Delay sign-in for as long as possible.** People often abandon apps when they’re forced to sign in before they can do anything useful. To help avoid this situation, give people a chance to get a sense of what your app or game does before asking them to make a commitment to it. For example, a shopping app might let people browse as much as they want, requiring sign-in only when they’re ready to make a purchase.
> 로그인을 가능한 한 오래 지연합니다. 사람들은 종종 유용한 일을 하기 전에 로그인해야 할 때 앱을 포기한다. 이러한 상황을 피하기 위해, 사람들에게 약속하도록 요청하기 전에 당신의 앱이나 게임이 무엇을 하는지 알 수 있는 기회를 주세요. 예를 들어, 쇼핑 앱은 사람들이 원하는 만큼 탐색할 수 있도록 하여 그들이 구매할 준비가 되었을 때만 로그인을 요구할 수 있다.
>




**If you don’t use Sign in with Apple in your iOS, iPadOS, or macOS app, prefer using a passkey.** Passkeys simplify account creation and authentication, eliminating the need for people to create or enter passwords. When an app enables passkeys, people simply provide their user name when creating a new account or signing in to an existing one. For developer guidance, see [Supporting passkeys](https://developer.apple.com/documentation/authenticationservices/public-private_key_authentication/supporting_passkeys). If you need to continue using passwords, use [Password AutoFill](https://developer.apple.com/documentation/security/password_autofill/) to automatically generate and fill in password and security code information.
> iOS, iPadOS 또는 macOS 앱에서 Apple과 함께 로그인을 사용하지 않는 경우 암호 키를 사용하는 것이 좋습니다. 암호는 계정 생성 및 인증을 단순화하므로 사용자가 암호를 만들거나 입력할 필요가 없습니다. 앱이 암호를 활성화하면, 사람들은 새 계정을 만들거나 기존 계정에 로그인할 때 사용자 이름만 제공합니다. 개발자 지침은 암호 지원을 참조하십시오. 암호를 계속 사용해야 하는 경우 암호 자동 채우기를 사용하여 암호 및 보안 코드 정보를 자동으로 생성하고 입력합니다.
>




**Always identify the authentication method you offer.** For example, if you display a button for signing in to your app with Face ID, title it using a phrase like “Sign In with Face ID” instead of a generic phrase like “Sign In.”
> 항상 제공하는 인증 방법을 식별하십시오. 예를 들어, Face ID로 앱에 로그인하기 위한 버튼을 표시하는 경우, "Sign In"과 같은 일반적인 문구 대신 "Sign In with Face ID"와 같은 문구를 사용하여 제목을 지정합니다.
>




**Refer only to authentication methods that are available in the current context.** For example, don’t reference Face ID on a device that doesn’t offer it. Check the device’s capabilities and use the appropriate terminology. For developer guidance, see [LABiometryType](https://developer.apple.com/documentation/localauthentication/labiometrytype).
> 현재 컨텍스트에서 사용할 수 있는 인증 방법만 참조하십시오. 예를 들어 Face ID를 제공하지 않는 장치에서 Face ID를 참조하지 마십시오. 장치의 기능을 확인하고 적절한 용어를 사용합니다. 개발자 지침은 LABiometryType을 참조하십시오.
>




**In general, avoid offering an app-specific setting for opting in to biometric authentication.** People enable biometric authentication at the system level, so presenting an in-app setting is redundant and could be confusing.
> 일반적으로 생체인증을 선택하기 위한 앱별 설정을 제공하지 마십시오. 사람들은 시스템 수준에서 생체 인증을 사용하므로 앱 내 설정을 표시하는 것은 중복되고 혼란스러울 수 있다.
>




**Avoid using the term *passcode* to refer to account authentication.** People create a passcode to unlock their device or authenticate for Apple services. If you use the term in your interface, people might think you’re asking them to reuse their passcode in your app or game.
> 계정 인증과 관련하여 암호라는 용어를 사용하지 마십시오. 사람들은 그들의 장치의 잠금을 해제하거나 애플 서비스에 대해 인증하기 위해 패스코드를 만든다. 인터페이스에서 이 용어를 사용하면 앱이나 게임에서 암호를 다시 사용하도록 요청한다고 생각할 수 있습니다.
>




# **Deleting accounts**

If you help people create an account within your app or game, you must also help them delete it, not just deactivate it. In addition to following the guidelines below, be sure to understand and comply with your region’s legal requirements related to account deletion and the right to be forgotten.
> 만약 당신이 다른 사람들이 당신의 앱이나 게임 안에 계정을 만드는 것을 돕는다면, 당신은 그것을 단지 비활성화하는 것이 아니라 그들이 그것을 삭제하도록 도와야 한다. 아래 지침을 따르는 것 외에도 계정 삭제 및 잊혀질 권리와 관련된 해당 지역의 법적 요구 사항을 이해하고 준수해야 합니다.
>




**IMPORTANT**If legal requirements compel your app to maintain accounts or information — such as digital health records — or to follow a specific account-deletion process, clearly describe the situation so people can understand the information or accounts you must maintain and the process you must follow.
> 중요 법적 요구 사항으로 인해 앱에서 디지털 건강 기록과 같은 계정 또는 정보를 유지하거나 특정 계정 삭제 프로세스를 따르도록 강요하는 경우, 사용자가 유지해야 하는 정보 또는 계정과 따라야 하는 프로세스를 사람들이 이해할 수 있도록 상황을 명확하게 설명합니다.
>




**Provide a clear way to initiate account deletion within your app or game.** If people can’t perform account deletion within your app, you must provide a direct link to the webpage on which people can do so. Make the link easy to discover — for example, don’t bury it in your Privacy Policy or Terms of Service pages.
> 앱이나 게임 내에서 계정 삭제를 시작할 수 있는 명확한 방법을 제공합니다. 앱 내에서 계정 삭제를 수행할 수 없는 경우 사용자가 수행할 수 있는 웹 페이지에 대한 직접 링크를 제공해야 합니다. 링크를 쉽게 찾을 수 있도록 합니다. 예를 들어 개인 정보 보호 정책 또는 서비스 약관 페이지에 링크를 묻지 마십시오.
>




**DEVELOPER NOTE**If people used [Sign in with Apple](../technologies/sign-in-with-apple/introduction) to create an account within your app, you revoke the associated tokens when they delete their account. See [Revoke tokens](https://developer.apple.com/documentation/sign_in_with_apple/revoke_tokens).
> 개발자 참고 앱 내에서 사용자가 Apple에 로그인하여 계정을 생성하면 해당 계정을 삭제할 때 관련 토큰을 해지합니다. 토큰 취소를 참조하십시오.
>




**Provide a consistent account-deletion experience whether people perform it within your app or game or on the website.** For example, avoid making one version of the deletion flow longer or more complicated than the other.
> 앱이나 게임 내에서 또는 웹 사이트에서 수행하든 일관된 계정 삭제 경험을 제공합니다. 예를 들어, 한 버전의 삭제 흐름이 다른 버전보다 길거나 복잡하지 않도록 하십시오.
>




**Consider letting people schedule account deletion to occur in the future.** People can appreciate the opportunity to use their remaining services or wait until their subscription auto-renews before deleting their account. If you offer a way to schedule account deletion, offer an option for immediate deletion as well.
> 나중에 계정 삭제를 예약하도록 하는 것을 고려해 보십시오. 사용자는 남은 서비스를 사용할 수 있는 기회를 높이 평가하거나 계정을 삭제하기 전에 가입이 자동으로 갱신될 때까지 기다릴 수 있습니다. 계정 삭제를 예약할 수 있는 방법을 제공하는 경우 즉시 삭제할 수도 있습니다.
>




**Tell people when account deletion will complete, and notify them when it’s finished.** Because it can sometimes take a while to fully delete an account, it’s essential to keep people informed about the status of the deletion process so they know what to expect.
> 계정 삭제가 언제 완료되는지 사람들에게 알려주고, 완료되면 알려준다. 계정을 완전히 삭제하는 데 때때로 시간이 걸릴 수 있으므로, 사람들이 무엇을 예상해야 하는지 알 수 있도록 삭제 프로세스의 상태에 대해 계속 알려주는 것이 중요합니다.
>




**If you support in-app purchases, help people understand how billing and cancellation work when they delete their account.** For example, you might need to help people understand the following scenarios:
> 앱 내 구매를 지원하는 경우, 계정을 삭제할 때 청구 및 취소가 어떻게 작동하는지 이해할 수 있도록 도와줍니다. 예를 들어, 다음과 같은 시나리오를 이해하도록 사용자를 도와야 할 수 있습니다.
>




- Billing for an auto-renewable subscription continues through Apple until people cancel the subscription, regardless of whether they delete their account.
- >  자동 갱신 구독에 대한 청구는 계정 삭제 여부와 상관없이 사람들이 구독을 취소할 때까지 애플을 통해 계속된다.

- After they delete their account, people need to cancel their subscription or request a refund.
- >  그들이 그들의 계정을 삭제한 후, 사람들은 그들의 구독을 취소하거나 환불을 요청해야 한다.


In addition to helping people understand these scenarios, provide information that describes how to cancel subscriptions and manage purchases. For guidance, see [Helping people manage their subscriptions](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/auto-renewable-subscriptions/#helping-people-manage-their-subscriptions) and [Providing help with In-App Purchases](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase/introduction/#providing-help-with-in-app-purchases).
> 사용자가 이러한 시나리오를 이해하는 데 도움이 될 뿐만 아니라 구독을 취소하고 구매를 관리하는 방법을 설명하는 정보를 제공합니다. 자세한 내용은 구독 관리 지원 및 앱 내 구매에 대한 도움말 제공을 참조하십시오.
>




**NOTE**Even if people didn’t use your app to purchase the subscription, you still need to enable account deletion.
> 참고. 다른 사용자가 구독을 구입하기 위해 앱을 사용하지 않았더라도 계정 삭제를 활성화해야 합니다.
>




# **TV provider accounts**

Many popular TV providers let people sign in to their accounts at the system level, eliminating the need to authenticate on an app-by-app basis. If your TV provider app requires people to sign in, use TV Provider Authentication to provide the most efficient onboarding experience.
> 많은 인기 TV 제공업체는 사람들이 시스템 수준에서 계정에 로그인할 수 있도록 허용하여 앱별로 인증할 필요가 없습니다. TV 공급자 앱에 로그인해야 하는 경우 TV 공급자 인증을 사용하여 가장 효율적인 온보드 환경을 제공합니다.
>




**Avoid displaying a sign-out option when people are signed in at the system level.** If your app must include a sign-out option, invoking it should prompt people to navigate to Settings > TV Provider to sign out of their account.
> 사용자가 시스템 수준에서 로그인할 때 로그아웃 선택사항을 표시하지 않도록 합니다. 앱에 로그아웃 옵션이 포함되어 있어야 하는 경우, 앱을 호출하면 설정 > TV 공급자로 이동하여 계정에서 로그아웃하라는 메시지가 나타납니다.
>




**Never instruct people to sign out by adjusting privacy controls.** The TV provider controls in Settings > Privacy aren’t a sign-out mechanism. These settings help people manage the apps that can access their TV provider account.
> 개인 정보 보호를 조정하여 사람들에게 로그아웃하도록 지시하지 마십시오. 설정 > 개인 정보 보호의 TV 제공자 제어는 로그아웃 메커니즘이 아닙니다. 이러한 설정은 사람들이 TV 공급자 계정에 액세스할 수 있는 앱을 관리하는 데 도움이 됩니다.
>




# **Platform considerations**

*No additional considerations for iOS, iPadOS, or macOS.*
> iOS, iPadOS 또는 macOS에 대한 추가 고려 사항은 없습니다.
>




# **tvOS**

