# **[technologies] sign-in-with-apple**

# Sign in with Apple provides a fast, private way to sign into apps and websites, giving people a consistent experience they can trust and the convenience of not having to remember multiple accounts and passwords.
> Apple 로그인은 앱과 웹 사이트에 로그인하는 빠르고 사적인 방법을 제공하여 사람들에게 신뢰할 수 있는 일관된 경험을 제공하고 여러 계정과 암호를 기억할 필요가 없는 편리함을 제공합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-SIWA-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-SIWA-intro_2x.png)

Supporting Sign in with Apple lets people use the Apple ID they already have to sign in or sign up, and skip filling out forms, verifying email addresses, and choosing passwords. In cases where you choose to ask for a name and email address, people have the option to share a unique, random email address that automatically relays messages to their personal email address. For developer guidance, see [Authentication Services](http://developer.apple.com/documentation/authenticationservices).
> Apple로 로그인을 지원하면 이미 로그인하거나 등록해야 하는 Apple ID를 사용할 수 있으며 양식 작성, 전자 메일 주소 확인 및 암호 선택을 생략할 수 있습니다. 이름과 전자 메일 주소를 묻기로 선택한 경우 사용자는 메시지를 자동으로 개인 전자 메일 주소로 릴레이하는 고유한 임의 전자 메일 주소를 공유할 수 있습니다. 개발자 지침은 인증 서비스를 참조하십시오.
>




You can offer Sign in with Apple in every version of your app or website across all platforms — including non-Apple platforms.
> Apple 이외의 플랫폼을 포함한 모든 플랫폼의 모든 버전 또는 웹 사이트에서 Apple로 로그인을 제공할 수 있습니다.
>




Sign in with Apple makes it easy for people to authenticate with Face ID or Touch ID and has two-factor authentication built in for an added layer of security. Apple does not use Sign in with Apple to profile users or their activity in apps.
> 애플 로그인은 사람들이 페이스ID나 터치ID로 쉽게 인증할 수 있게 해주며, 보안 계층을 강화하기 위해 2단계 인증이 내장되어 있다. Apple은 Apple에서 사용자 또는 사용자의 앱 활동을 프로파일링하는 데 Apple 로그인을 사용하지 않습니다.
>




# **Offering Sign in with Apple**
> Apple로 로그인 제공
>




Follow these guidelines to offer Sign in with Apple when it’s most convenient for people.
> 다음 지침에 따라 사용자가 가장 편리할 때 Apple에 로그인할 수 있습니다.
>




**Ask people to sign in only in exchange for value.** People need to understand why you’re asking them to sign in, so it can work well to display a brief, approachable description of sign-in benefits. For example, you might want to tell people that signing in lets them personalize the app experience, access additional features, or synchronize data.
> 사람들에게 가치를 대가로 로그인하도록 요청하십시오. 사람들은 사용자가 로그인을 요청하는 이유를 이해해야 로그인 혜택에 대한 간략하고 접근 가능한 설명을 표시할 수 있습니다. 예를 들어, 로그인을 통해 앱 경험을 개인화하거나, 추가 기능에 액세스하거나, 데이터를 동기화할 수 있다고 사람들에게 말하고 싶을 수 있습니다.
>




**Delay sign-in as long as possible.** People often abandon apps when they’re forced to sign in before doing anything useful. Give them a chance to familiarize themselves with your app before making a commitment. For example, a live-streaming app could let people explore available content before signing in to stream something.
> 사람들은 유용한 일을 하기 전에 강제로 로그인해야 할 때 앱을 버리는 경우가 많습니다. 약속을 하기 전에 그들에게 당신의 앱에 익숙해질 기회를 주세요. 예를 들어, 라이브 스트리밍 앱은 사람들이 무언가를 스트리밍하기 위해 로그인하기 전에 이용 가능한 콘텐츠를 탐색하도록 할 수 있다.
>




**If you require an account, ask people to set it up before offering any sign-in options.** Start by explaining the reasons for requiring an account. Then, after people complete account setup, let them choose a convenient way to sign in to their new account by offering Sign in with Apple and any other sign-in methods you support.
> 계정이 필요한 경우 로그인 옵션을 제공하기 전에 계정을 설정하도록 요청하십시오. 계정이 필요한 이유를 설명하는 것부터 시작하십시오. 그런 다음 사용자가 계정 설정을 완료한 후 Apple 로그인 및 지원하는 다른 로그인 방법을 제공하여 새 계정에 편리하게 로그인할 수 있는 방법을 선택하도록 합니다.
>




**Consider letting people link an existing account to Sign in with Apple.** When you support this type of linking, people can get the convenience of using Sign in with Apple while maintaining access to the information in an account they’ve already set up. You can offer account linking before or after people sign in to their existing account. For example:
> 사용자가 기존 계정을 Apple로 로그인하도록 허용하는 것을 고려해 보십시오. 이러한 유형의 링크를 지원하면 이미 설정한 계정의 정보에 대한 액세스를 유지하면서 Apple로 로그인을 사용할 수 있습니다. 사용자가 기존 계정에 로그인하기 전이나 후에 계정 연결을 제공할 수 있습니다. 예:
>




- If people share an email address through Sign in with Apple and it matches the address in an existing account, you can suggest that they link Sign in with Apple to that account.
- >  사용자가 Apple과 로그인을 통해 이메일 주소를 공유하고 기존 계정의 주소와 일치하는 경우 해당 계정에 로그인을 연결하도록 제안할 수 있습니다.

- If people used an existing username and password to sign in, you can display an account-linking suggestion in their account’s settings view or another logical place.
- >  사용자가 기존 사용자 이름과 암호를 사용하여 로그인한 경우 계정 설정 보기 또는 다른 논리적 위치에 계정 연결 제안을 표시할 수 있습니다.


**In a commerce app, wait until after people make a purchase before asking them to create an account.** If you support a guest checkout system, give people a quick way to create an account after the transaction completes. For example, if you support Apple Pay, let people create an account on the order confirmation page. In cases where people have already provided their name and email address during the Apple Pay transaction, you don’t need to ask for this information.
> 커머스 앱에서, 사람들이 계정을 만들도록 요청하기 전에 사람들이 구매를 할 때까지 기다리십시오. 만약 당신이 게스트 체크아웃 시스템을 지원한다면, 사람들에게 거래가 완료된 후에 계정을 만들 수 있는 빠른 방법을 제공하십시오. 예를 들어, Apple Pay를 지원하는 경우 주문 확인 페이지에서 사용자가 계정을 만들 수 있습니다. Apple Pay 거래 중에 사용자가 이미 이름과 전자 메일 주소를 제공한 경우에는 이 정보를 요청할 필요가 없습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/create-account-after-purchase_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/sign-in-with-apple/images/create-account-after-purchase_2x.png)

**As soon as Sign in with Apple completes, welcome people to their new account.** Help people use their new account right away; don’t delay the experience by asking for information that isn’t required.
> Apple 로그인이 완료되는 대로 새 계정으로 오신 것을 환영합니다. 새 계정을 바로 사용할 수 있도록 도와주십시오. 불필요한 정보를 요청하여 경험을 지연시키지 마십시오.
>




**Indicate when people are currently signed in.** You can help people confirm their sign-in method by displaying a phrase like “Using Sign in with Apple” in places like a settings or account interface.
> 사용자가 현재 로그인한 시간을 나타냅니다. 설정 또는 계정 인터페이스와 같은 위치에 "Apple에서 로그인 사용"과 같은 문구를 표시하여 사용자가 로그인 방법을 확인하도록 도와줄 수 있습니다.
>




# **Collecting data**

People appreciate Sign in with Apple for its privacy and convenience. Although some apps or websites may require additional information — such as a date of birth or a region of residence — it’s essential to minimize your requests for data as people set up an account. Build on the trust that people have in Sign in with Apple by describing why you need additional data and clearly displaying the data you receive.
> 사람들은 애플사의 사생활과 편리함에 대해 애플사에 로그인하는 것을 높이 평가한다. 일부 앱이나 웹 사이트에는 생년월일이나 거주 지역과 같은 추가 정보가 필요할 수 있지만, 사람들이 계정을 설정할 때 데이터에 대한 요청을 최소화하는 것이 중요합니다. 추가 데이터가 필요한 이유를 설명하고 수신한 데이터를 명확하게 표시하여 Apple에 로그인하는 사용자의 신뢰를 기반으로 합니다.
>




**Clarify whether the additional data you request is required or just recommended.** If the data is legally or contractually required — such as an agreement to terms of service, country or region of residence, birth date, or information required by a region’s real-identity laws — make sure people understand that they must supply the additional information to complete the setup of their account. If additional data isn’t required but can improve the user experience, make sure people know the request is optional and help them understand the benefits of providing the information.
> 요청하는 추가 데이터가 필요한지 아니면 단지 권장되는 것인지를 명확히 합니다. 서비스 조건, 국가 또는 거주 지역, 생년월일 또는 지역의 실제 신분법에 의해 요구되는 정보와 같이 법적 또는 계약적으로 데이터가 필요한 경우 사람들은 다음 사이트에서 추가 정보를 제공해야 한다는 것을 이해해야 합니다계정 설정을 완료해야 합니다. 추가 데이터가 필요하지 않지만 사용자 환경을 개선할 수 있는 경우, 사용자가 요청이 선택 사항임을 알고 정보 제공의 이점을 이해할 수 있도록 도와주십시오.
>




**Don’t ask people to supply a password.** A key benefit of Sign in with Apple is that people don’t have to create and memorize additional passwords. Unless people have stopped using Sign in with Apple with your app or website, don’t ask for a password.
> 사람들에게 비밀번호를 제공하라고 요구하지 마세요. 애플 로그인의 주요 이점은 사람들이 추가적인 비밀번호를 만들고 기억할 필요가 없다는 것입니다. 앱이나 웹 사이트에서 Apple 로그인 사용을 중지한 사람이 아니라면 암호를 묻지 마십시오.
>




**Avoid asking for a personal email address when people supply a private relay address.** Using Sign in with Apple, people can choose to share a private relay address that automatically forwards messages to their verified personal email account. It’s essential to respect this choice and avoid overriding it by asking for a personal email address. If you present customer service, retail, or other experiences that request identification via email address, you can:
> 사람들이 개인 릴레이 주소를 제공할 때 개인 전자 메일 주소를 묻는 것을 피하십시오. Apple에서 로그인을 사용하면 확인된 개인 전자 메일 계정으로 메시지를 자동으로 전달하는 개인 릴레이 주소를 공유하도록 선택할 수 있습니다. 이 선택을 존중하고 개인 이메일 주소를 요청하여 이를 무시하지 않는 것이 중요합니다. 이메일 주소를 통해 식별을 요청하는 고객 서비스, 소매 또는 기타 경험을 제시하는 경우 다음을 수행할 수 있습니다:
>




- Make sure that people can view their private relay address in your app or website
- >  사용자가 앱 또는 웹 사이트에서 개인 릴레이 주소를 볼 수 있는지 확인합니다

- Direct people to Settings > Apple ID > Password & Security > Apps using Apple ID to retrieve their private relay address
- >  설정 > Apple ID > 비밀번호 및 보안 > Apple ID를 사용하여 개인 릴레이 주소를 검색하는 앱으로 이동합니다

- Use other identifying values, like an order number or phone number collected as part of a purchase
- >  구매의 일부로 수집된 주문 번호 또는 전화 번호와 같은 다른 식별 값 사용


**Give people a chance to engage with your app before asking for optional data.** As people use your app, you can help them discover places where they can benefit from sharing more information with you. For example, you might suggest that they provide a contact phone number if they want real-time text updates, or social network information if they want to play games with friends. If people choose not to provide optional information, don’t prevent them from accessing their account or using all the features of your app.
> 선택적 데이터를 요청하기 전에 사용자의 앱에 참여할 수 있는 기회를 제공합니다. 사용자가 사용자의 앱을 사용할 때 사용자와 더 많은 정보를 공유하여 이익을 얻을 수 있는 장소를 찾을 수 있도록 도와줄 수 있습니다. 예를 들어 실시간 텍스트 업데이트를 원하는 경우 연락처 전화 번호를 제공하거나 친구와 게임을 하려는 경우 소셜 네트워크 정보를 제공할 것을 제안할 수 있습니다. 사용자가 선택적 정보를 제공하지 않기로 선택한 경우 사용자가 자신의 계정에 액세스하거나 앱의 모든 기능을 사용하는 것을 막지 마십시오.
>




