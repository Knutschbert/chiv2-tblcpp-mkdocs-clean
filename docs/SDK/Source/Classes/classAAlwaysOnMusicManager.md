---
title: AAlwaysOnMusicManager
type: class
aliases: AAlwaysOnMusicManager
share: false

---

# AAlwaysOnMusicManager





Inherits from [ATBLActor](/docs/SDK/Source/Classes/classATBLActor.md), AActor, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[AAlwaysOnMusicManager]]**() |
| EAlwaysOnMusicState | **[[GetCurrentMusicState]]**() |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| void | **[[OnRep_AlwaysOnMusicState]]**() |
| void | **[[SetCurrentMusicState]]**(EAlwaysOnMusicState NewState) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| UAkComponent * | **[[AkComponent]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200