# **[patterns] ratings-and-reviews**

# People often view the ratings and reviews for an app or game before they download it.
> 사람들은 종종 앱이나 게임의 평점과 리뷰를 다운로드하기 전에 본다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-ratings-and-reviews-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-ratings-and-reviews-intro-dark_2x.png)

Delivering a great overall experience is the best way to encourage positive ratings and reviews, but it’s also crucial to choose the right time to ask people for feedback. Although every app is different, some possible ways to do this involve looking at how many times or how frequently people launch your app, the number of features someone explores, or the number of tasks they complete.
> 좋은 전반적인 경험을 제공하는 것이 긍정적인 평가와 평가를 장려하는 가장 좋은 방법이지만, 사람들에게 피드백을 요청할 수 있는 적절한 시기를 선택하는 것도 중요하다. 모든 앱이 다르지만, 이 작업을 수행하는 몇 가지 가능한 방법에는 사용자가 앱을 얼마나 자주 실행하는지, 탐색하는 기능의 수 또는 완료되는 작업의 수를 확인하는 방법이 포함됩니다.
>




People can always rate your app within the App Store.
> 사람들은 앱 스토어에서 항상 당신의 앱을 평가할 수 있다.
>




# **Best practices**

**Ask for a rating only after people have demonstrated engagement with your app or game.** For example, you might prompt people when they complete a game level or a significant task. Avoid asking for a rating on first launch or during onboarding, because people haven’t had enough time to gain a clear understanding of your app's value or form an opinion. People may even be more likely to leave negative feedback if they feel an app is asking for a rating before they get a chance to use it.
> 사람들이 당신의 앱이나 게임에 참여했다는 것을 증명한 후에만 등급을 요청하세요. 예를 들어, 게임 수준이나 중요한 작업을 완료하면 메시지를 표시할 수 있습니다. 앱의 가치를 명확히 이해하거나 의견을 형성하기 위해 충분한 시간이 없었기 때문에 첫 출시 시 또는 온보딩 중에 등급을 묻는 것을 피하십시오. 사람들은 앱이 그것을 사용할 기회를 얻기 전에 등급을 물어본다고 느낀다면 부정적인 피드백을 남길 가능성이 더 높을 것이다.
>




**Avoid interrupting people while they're performing a task or playing a game.** Asking for feedback can disrupt the user experience and feel like a burden. Look for natural breaks or stopping points in your app or game where a rating request is less likely to be bothersome.
> 사람들이 작업을 수행하거나 게임을 하는 동안 방해하지 마십시오. 피드백을 요청하는 것은 사용자 경험을 방해하고 부담으로 느낄 수 있다. 당신의 앱이나 게임에서 등급 요청이 덜 번거로울 수 있는 자연스러운 중단점이나 정지점을 찾으세요.
>




**Avoid pestering people.** Repeated rating requests can be irritating, and may even negatively influence people’s opinion of your app. Consider allowing at least a week or two between requests, prompting again after people demonstrate additional engagement with your experience.
> 사람을 귀찮게 하지 마라. 반복적인 평가 요청은 짜증날 수 있으며, 심지어 당신의 앱에 대한 사람들의 의견에 부정적인 영향을 미칠 수 있다. 요청 사이에 최소 1주일 또는 2주 정도 시간을 두고, 사람들이 귀하의 경험에 대한 추가 참여를 입증한 후 다시 요청하는 것을 고려해 보십시오.
>




**Prefer the system-provided prompt.** iOS, iPadOS, and macOS offer a consistent, nonintrusive way for apps and games to request ratings and reviews. When you identify places in your experience where it makes sense to ask for feedback, the system checks for previous feedback and — if there isn’t any — displays an in-app prompt that asks for a rating and an optional written review. People can supply feedback or dismiss the prompt with a single tap or click; they can also opt out of receiving these prompts for all apps they have installed. The system automatically limits the display of the prompt to three occurrences per app within a 365-day period. For developer guidance, see [SKStoreReviewController](https://developer.apple.com/documentation/storekit/skstorereviewcontroller).
> 시스템이 제공하는 프롬프트를 선택합니다. iOS, iPadOS 및 macOS는 앱과 게임이 등급 및 리뷰를 요청할 수 있는 일관된 비침해적 방법을 제공합니다. 사용자 경험에서 피드백을 요청하는 것이 적합한 장소를 식별하면 시스템은 이전 피드백을 확인하고, 피드백이 없는 경우 앱 내 프롬프트를 표시하여 평가 및 서면 검토(선택 사항)를 요청합니다. 사용자는 한 번의 탭이나 클릭으로 피드백을 제공하거나 프롬프트를 무시할 수 있으며, 설치한 모든 앱에 대해 이러한 프롬프트를 수신하지 않을 수도 있습니다. 시스템은 365일 기간 내에 앱당 3회로 프롬프트 표시를 자동으로 제한한다. 개발자 지침은 SKStoreReviewController를 참조하십시오.
>




**Weigh the benefits of resetting your summary rating against the potential disadvantage of showing fewer ratings.** When you release a new version of your app or game, you can reset the summary of individual ratings you received since the last reset. Although resetting means that the ratings reflect the current version, it also tends to result in having fewer ratings overall, which can discourage some people from downloading your app. For developer guidance, see [Reset app summary rating](https://help.apple.com/app-store-connect/#/devfb7e87af8).
> 요약 등급을 재설정하면 얻을 수 있는 이점과 더 적은 등급을 표시하면 얻을 수 있는 잠재적인 단점을 비교해 보십시오. 앱이나 게임의 새 버전을 출시할 때 마지막 재설정 이후 받은 개별 등급의 요약을 재설정할 수 있습니다. 재설정한다는 것은 등급이 현재 버전을 반영한다는 것을 의미하지만 전반적으로 등급이 낮아지는 경향이 있어 일부 사람들이 앱을 다운로드하지 못하게 할 수 있습니다. 개발자 지침은 앱 요약 등급 재설정을 참조하십시오.
>




# **Platform considerations**

*No additional considerations for iOS, iPadOS, macOS, tvOS, or watchOS.*
> iOS, iPadOS, macOS, tvOS 또는 워치에 대한 추가 고려 사항 없음OS.
>



