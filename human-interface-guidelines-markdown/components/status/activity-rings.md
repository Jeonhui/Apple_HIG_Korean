Activity rings
==============

Activity rings show an individual’s daily progress toward Move, Exercise, and Stand goals.![A stylized representation of a set of move, exercise, and stand activity rings denoting progress. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/715b90d471efa2d8c388287bc5fe1700/components-activity-ring-intro@2x.png)

In watchOS, the Activity ring element always contains three rings, whose colors and meanings match those the Activity app provides. In iOS, the Activity ring element contains either a single Move ring representing an approximation of activity, or all three rings if an Apple Watch is paired.

[Best practices](/design/human-interface-guidelines/activity-rings#Best-practices)
----------------------------------------------------------------------------------

**Display Activity rings when they’re relevant to the purpose of your app.** Activity rings are an important component of the Apple Watch experience. If your app is related to health or fitness, and especially if it contributes information to HealthKit, people generally expect to find Activity rings in your interface. For example, if you structure a workout or health session around the completion of Activity rings, consider displaying the element on a workout metrics screen so that people can track their progress during their session. Similarly, if you provide a summary screen that appears at the conclusion of a workout, you could display Activity rings to help people check on their progress toward their daily goals.

![A screenshot of an in-progress workout screen that displays the current timer value, followed by a list of the current Move, Exercise, and Stand values. The screen also displays an image of the Activity rings, where the state of each ring represents the current value.](https://docs-assets.developer.apple.com/published/acfdc1f7c5034f663ade56a921c377e3/activity-rings-summary@2x.png)**Use Activity rings only to show Move, Exercise, and Stand information.** Activity rings are designed to consistently represent progress in these specific areas. Don’t attempt to replicate or modify Activity rings for other purposes. Never use Activity rings to display other types of data. Never show Move, Exercise, and Stand progress in another ring-like element.

**Use Activity rings to show progress for a single person.** Never use Activity rings to represent data for more than one person, and make sure it’s obvious whose progress you’re showing by using a label, a photo, or an avatar.

**Maintain Activity ring colors.** For a consistent experience, keep the visual appearance of Activity rings the same regardless of the context in which they appear. Never change the look of the rings by using filters, changing colors, or modifying opacity. Instead, design the surrounding interface to blend with the rings. For example, enclose the rings and background within a circle. Always scale the rings appropriately so they don’t seem disconnected or out of place.

**Always display Activity rings on a black background.** The background is a key component of Activity ring presentation. Don’t display the rings on anything other than a black background.

**Maintain Activity ring margins.** An Activity ring element must include a minimum outer margin of no less than the distance between rings. Never allow other elements to crop, obstruct, or encroach upon this margin or the rings themselves. To display an Activity ring element within a circle, adjust the corner radius of the enclosing view rather than applying a circular mask.

**Differentiate other ring-like elements from Activity rings.** Mixing different ring styles can lead to a visually confusing interface. If you must include other rings, use padding, lines, or labels to separate them from Activity rings. Color and scale can also help provide visual separation.

**Don’t send notifications that repeat the same information the Activity app sends.** The system already delivers Move, Exercise, and Stand progress updates, so it’s confusing for people to receive redundant information from your app. Also, don’t show an Activity ring element in your app’s notifications. It’s fine to reference Activity progress in a notification, but do so in a way that’s unique to your app and doesn’t replicate the same information the system provides.

**Don’t use Activity rings for ornamentation.** Activity rings provide information to people, not embellish your app’s design. Never display Activity rings in labels or background graphics.

**Don’t use Activity rings for branding.** Use Activity rings strictly to display Activity progress in your app. Never use Activity rings in your app’s icon or marketing materials.

[Platform considerations](/design/human-interface-guidelines/activity-rings#Platform-considerations)
----------------------------------------------------------------------------------------------------

*No additional considerations for iPadOS or watchOS. Not supported in macOS, tvOS, or visionOS.*

### [iOS](/design/human-interface-guidelines/activity-rings#iOS)

Activity rings are available in iOS with [`HKActivityRingView`](/documentation/healthkit/hkactivityringview)
. The appearance of the Activity ring element changes automatically depending on whether an Apple Watch is paired:

* With an Apple Watch paired, iOS shows all three Activity rings.
* Without an Apple Watch paired, iOS shows the Move ring only, which represents an approximation of a person’s activity based on their steps and workout information from other apps.

Because iOS shows Activity rings whether or not an Apple Watch is paired, activity history can include a combination of both styles. For example, Activity rings in Fitness have three rings when a person exercises with their Apple Watch paired, and only the Move ring when they exercise without their Apple Watch.

[Resources](/design/human-interface-guidelines/activity-rings#Resources)
------------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/activity-rings#Related)

[Workouts](/design/human-interface-guidelines/workouts)


#### [Developer documentation](/design/human-interface-guidelines/activity-rings#Developer-documentation)

[`HKActivityRingView`](/documentation/healthkit/hkactivityringview)


[`WKInterfaceActivityRing`](/documentation/watchkit/wkinterfaceactivityring)


