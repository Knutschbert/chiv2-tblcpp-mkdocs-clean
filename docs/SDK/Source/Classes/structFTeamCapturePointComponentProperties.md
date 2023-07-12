---
title: FTeamCapturePointComponentProperties
type: struct
aliases: FTeamCapturePointComponentProperties
share: false

---

# FTeamCapturePointComponentProperties





## Public Functions

|                | Name           |
| -------------- | -------------- |
| TBL_API | **[[FTeamCapturePointComponentProperties]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| bool | **[[AllowBots]]**  |
| bool | **[[AllowKillBonusInsideCaptureVolume]]**  |
| bool | **[[AllowNPCs]]**  |
| TArray< EFaction > | **[[AllowedFactions]]**  |
| [FDataTableRowSelection](/docs/SDK/Source/Classes/structFDataTableRowSelection.md) | **[[AttackerKillScoringRow]]**  |
| bool | **[[AutoNeutralizeTeamCapturePoint]]**  |
| TEnumAsByte< ECaptureVolumeControlType::Type > | **[[CapturePointRule]]**  |
| [FDataTableRowSelection](/docs/SDK/Source/Classes/structFDataTableRowSelection.md) | **[[DefenderKillScoringRow]]**  |
| EFaction | **[[DefendingFaction]]**  |
| TMap< EFaction, TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > > | **[[FactionClassRequirement]]**  |
| float | **[[ImmunityTimeAfterActivation]]**  |
| float | **[[ImmunityTimeAfterCapture]]**  |
| int32 | **[[PlayersNeededToCapture]]**  |
| float | **[[TimeBetweenTickEvents]]**  |
| float | **[[TimeToCapture]]**  |
| float | **[[TimeToNeutralize]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:02 +0200