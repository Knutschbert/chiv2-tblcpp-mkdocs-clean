---
title: ATBLHUD
type: class
aliases: ATBLHUD
share: false

---

# ATBLHUD





Inherits from AHUD

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[ATBLHUD]]**() |
| void | **[[ClearHint]]**() |
| void | **[[DrawHUD]]**() |
| void | **[[DrawMaterialSimpleWithTriangles]]**(UMaterialInterface * Material, float ScreenX, float ScreenY, float ScreenW, float ScreenH) |
| void | **[[ForceClearHint]]**() |
| void | **[[GamepadHideEmoteWheel]]**() |
| void | **[[GamepadShowEmoteWheel]]**() |
| FVector2D | **[[GetCrosshairPositionInViewport]]**() |
| bool | **[[GetImportantMessage]]**([FImportantGameMsg](/docs/SDK/Source/Classes/structFImportantGameMsg.md) & ImportantMessageOut) |
| AActor * | **[[GetShowDebugTargetActor]]**() |
| void | **[[InGameMenuPressed]]**() |
| void | **[[InGameMenuReleased]]**() |
| void | **[[NotifyPossessedPawn]]**(APawn * NewPawn) |
| void | **[[OnPossessedPawn]]**(APawn * NewPawn) |
| void | **[[PS4TouchpadPressed]]**() |
| void | **[[ReleaseGuiBackgroundRequest]]**() |
| void | **[[RequestGuiBackground]]**(bool bImmediate) |
| void | **[[SetMiniMapVisibility]]**(bool Visible) |
| void | **[[SetShowDebugTargetActor]]**(AActor * Actor) |
| void | **[[ShowHint]]**(const FText & HintToShow, const FText & HintTitle, FName HintTableRowName) |
| void | **[[ShowIngameMenu]]**() |
| void | **[[ShowLoadoutScreen]]**() |
| void | **[[ShowLoadoutScreenFirstTime]]**() |
| void | **[[ShowTeamSelectScreen]]**(bool bGameStart) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[GetRadialVOMouseAngle]]**(int32 & ButtonIndex, bool & RadialDeselected, FVector2D & MousePositionByCanvas) |
| void | **[[SetRadialVOMaterial]]**(UMaterialInstanceDynamic * inRadialVOMID) |
| void | **[[ShowHideRadialEmote]]**(bool Show) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< [FAbilityDescriptionInfo](/docs/SDK/Source/Classes/structFAbilityDescriptionInfo.md) > | **[[AbilityDescriptionInfos]]**  |
| TArray< [FAbilityDrawInfo](/docs/SDK/Source/Classes/structFAbilityDrawInfo.md) > | **[[AbilityDrawInfos]]**  |
| AActor * | **[[ActorUnderCrosshair]]**  |
| float | **[[CrosshairChargingPercentage]]**  |
| FVector2D | **[[CrosshairOffset]]**  |
| UTexture * | **[[DragHUDTexture]]**  |
| FDrawDebugSignature | **[[DrawDebug]]**  |
| TArray< [FEffectDrawInfo](/docs/SDK/Source/Classes/structFEffectDrawInfo.md) > | **[[EffectDrawInfos]]**  |
| TArray< [FImportantGameMsg](/docs/SDK/Source/Classes/structFImportantGameMsg.md) > | **[[ImportantGameMessageQueue]]**  |
| float | **[[MaxActorUnderCrosshairDistance]]**  |
| FVector2D | **[[MouseDelta]]**  |
| int32 | **[[NextImportantMessageId]]**  |
| FBroadcastActorUnderCrosshairChangedEvent | **[[OnBroadcastActorUnderCrosshairChanged]]**  |
| FBroadcastCrosshairMessage | **[[OnBroadcastCrosshairMessage]]**  |
| FBroadcastObjectiveMessage | **[[OnBroadcastObjectiveMessage]]**  |
| FBroadcastSpecialSpawnEventCreated | **[[OnBroadcastSpecialSpawnEventCreated]]**  |
| float | **[[ProjectileControlRadius]]**  |
| float | **[[TimeToDelayShowingPostGame]]**  |
| bool | **[[bAbilityHasValidTarget]]**  |
| bool | **[[bDisableFriendlyIFFHudMarker]]**  |
| bool | **[[bDisableHud]]**  |
| bool | **[[bDrawHudMarkers]]**  |
| bool | **[[bEnableCrosshair]]**  |
| bool | **[[bEnableProjectileControl]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [FCombatHudMessage](/docs/SDK/Source/Classes/structFCombatHudMessage.md) | **[[CurrentCombatHudMessage]]**  |
| FVector2D | **[[DistanceFactorMultiplier]]**  |
| FLinearColor | **[[EnemyMarkerColor]]**  |
| float | **[[EnemyMarkerMaxDistance]]**  |
| FLinearColor | **[[EnemyNameFontColor]]**  |
| FLinearColor | **[[EnemyNameFontOutlineColor]]**  |
| float | **[[EnemyNameplateMaxDistance]]**  |
| TMap< EFaction, FLinearColor > | **[[FontColorsByFaction]]**  |
| TMap< EFaction, FLinearColor > | **[[FontOutlineColorsByFaction]]**  |
| FVector2D | **[[FriendlyHealthFullSize]]**  |
| UMaterialInterface * | **[[FriendlyIFFHudMarkerMaterial]]**  |
| FLinearColor | **[[FriendlyMarkerColor]]**  |
| float | **[[FriendlyMarkerMaxDistance]]**  |
| FLinearColor | **[[FriendlyNameFontColor]]**  |
| FLinearColor | **[[FriendlyNameFontOutlineColor]]**  |
| FLinearColor | **[[HealthBarEmptyColor]]**  |
| FLinearColor | **[[HealthBarFillColor]]**  |
| UMaterialInterface * | **[[HudMarkerCrossHairMaterial]]**  |
| float | **[[HudMarkerDetailsFadeEnd]]**  |
| float | **[[HudMarkerDetailsFadeStart]]**  |
| FVector2D | **[[HudMarkerDetailsFullSize]]**  |
| UMaterialInterface * | **[[HudMarkerDetailsMaterial]]**  |
| float | **[[HudMarkerDetailsOffsetPixels]]**  |
| float | **[[HudMarkerDetailsOpacity]]**  |
| FLinearColor | **[[HudMarkerFontColor]]**  |
| FSlateFontInfo | **[[HudMarkerFontInfo]]**  |
| FLinearColor | **[[HudMarkerFontOutlineColor]]**  |
| FLinearColor | **[[HudMarkerFontShadowColor]]**  |
| FVector2D | **[[HudMarkerFontShadowOffset]]**  |
| FVector2D | **[[HudMarkerFullSize]]**  |
| float | **[[HudMarkerMaxDistance]]**  |
| float | **[[HudMarkerMinimumScale]]**  |
| float | **[[HudMarkerOpacity]]**  |
| float | **[[HudMarkerReducedOpacity]]**  |
| FVector2D | **[[HudMarkerReducedSize]]**  |
| float | **[[HudMarkerReductionEnd]]**  |
| float | **[[HudMarkerReductionStart]]**  |
| UCurveFloat * | **[[HudMarkerScaleCurve]]**  |
| float | **[[HudMarkerScreenRadius]]**  |
| float | **[[HudMarkerTextOffsetPixels]]**  |
| FName | **[[IFFBoneName]]**  |
| FVector2D | **[[IFFHudMarkerFullSize]]**  |
| float | **[[IFFHudMarkerOpacity]]**  |
| float | **[[IFFHudMarkerReducedOpacity]]**  |
| FVector2D | **[[IFFHudMarkerReducedSize]]**  |
| FVector | **[[IFFOffset]]**  |
| int32 | **[[MaxPlayerNameCharsToRender]]**  |
| float | **[[NonVisiblePawnMarkerOpacity]]**  |
| FVector2D | **[[OffscreenPlayerFakeSize]]**  |
| float | **[[PlayerNameDistFadeMax]]**  |
| float | **[[PlayerNameDistFadeMin]]**  |
| FSlateFontInfo | **[[PlayerNameFontInfo]]**  |
| FLinearColor | **[[PlayerNameFontShadowColor]]**  |
| FVector2D | **[[PlayerNameFontShadowOffset]]**  |
| float | **[[PlayerNameOffsetPixels]]**  |
| TArray< FVector2D > | **[[RadialAngles]]**  |
| float | **[[RadialCentreRadiusSizeSquared]]**  |
| float | **[[RadialMouseSensitivity]]**  |
| UMaterialInstanceDynamic * | **[[RadialVOMID]]**  |
| float | **[[TimeLengthOfCrosshairMessages]]**  |
| float | **[[TimeLengthOfObjectiveMessages]]**  |
| bool | **[[bClampPlayerMarkersToScreen]]**  |
| bool | **[[bDisablePlayerNamePlates]]**  |
| bool | **[[bDisplayFriendlyHealth]]**  |
| bool | **[[bIsHudMarkerFontOutlined]]**  |
| bool | **[[bIsHudMarkerFontShadowed]]**  |
| bool | **[[bIsPlayerNameFontOutlined]]**  |
| bool | **[[bIsPlayerNameFontShadowed]]**  |
| bool | **[[bOnlyShowMarkersOnVisiblePawns]]**  |
| bool | **[[bOnlyShowNamesOnTeammates]]**  |
| bool | **[[bUseTeamColorForHealthBar]]**  |
| bool | **[[bUseTeamColorForIffMarkerAndNameplate]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200