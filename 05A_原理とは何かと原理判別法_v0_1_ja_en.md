# 原理とは何か／原理判別法
## ― 観測・パターン・モデル・機構を原理へ誤昇格させないための認知工学的判別仕様 ―

**版**：v0.1  
**改訂日**：2026-10-07  
**著者**：がっちむち♂  
**文章生成支援**：LLM  
**原典言語**：日本語  

> **翻訳階層規定**：Part I = J0 日本語正本。Part II = T2 / English Summary Projection。T2は全文翻訳ではなく、独立した正本・規定文書ではない。意味衝突・欠落・曖昧さ・翻訳残差がある場合はJ0を優先し、下流側で新規主張を補わない。詳細は `TRANSLATION_POLICY.md`。

> **位置づけ**：本稿は認知工学における「原理」の現行定義と、その判別方法を公開可能な粒度で規定する。HDS内部の具体的原理発見手順・評価器・実装レシピを公開するものではない。

> **理論状態規定**：原理、原理候補、必要性、最小性、同型、因果、成立、崩壊という語・関係自体も時点付きProjectionである。本稿は現行版内部では判別可能性のため意味を固定するが、最終不変の存在論へ昇格しない。

---

# Part I. 日本語原典

## 1行定義

> **原理とは、特定時点・認知世界・主体・対象・関係・条件の下で、「何が、どの関係によって、どの条件で、何を成立・変化させ、何を変えれば崩れるか」を説明する構造核である。**

原理は、単なる観測結果でも、頻出パターンでも、もっともらしい説明でもない。

そして現行認知工学では、

> **原理は絶対真理として発見されるのではなく、適用範囲・時点・反証条件・再開放条件を持つ暫定原理として採用される。**

---

# 0. 原理質問

原理判別の出発点は、

> **何がこれを成立させているのか。**

である。

この「これ」には、

- 現象
- 判断
- 意思決定
- 能力
- 結果
- 制度
- 理論
- 証明
- 安全性
- 再現性
- 失敗

等を含み得る。

ただし最初に得た説明を特権化しない。

一つの説明が出た時点では、まだ原理ではない。

---

# 1. 原理と下位記述を分ける

原理判別では、少なくとも次を混同しない。

| 状態 | 現行定義 |
|---|---|
| 観測 | 何が起きたか |
| 共通点 | 複数事例に同じ特徴がある |
| 相関 | 複数量・状態が共変する |
| パターン | 反復して現れる形・傾向 |
| モデル | 対象を扱うための記述・表現 |
| 機構 | どう作用・遷移して結果へ至るかという過程候補 |
| 原理候補 | 複数の観測・機構・結果を成立させる構造核の候補 |
| 適用範囲付き暫定原理 | 現行条件で判別ゲートを通過し、局所適用可能とされた構造核 |

したがって、

```text
よく出る
≠
原理

説明できる
≠
原理

相関がある
≠
原理

機構が書ける
≠
原理
```

である。

---

# 2. 原理候補の最低記述

原理候補Pは、最低でも次へ答えられなければならない。

```text
1. 何が作用するのか
2. 何と何がどの関係にあるのか
3. どの条件で成立するのか
4. 何を成立・維持・変化させるのか
5. 何を変えると崩れるのか
6. 何が観測されたら反証・改訂対象になるのか
7. どこまでが適用範囲か
```

これらを分別できない場合、原理ではなく、

```text
未形成
原理の影
パターン
モデル
機構候補
原理候補
```

等の下位状態として保持する。

分別不足を、語の強さで原理へ昇格させない。

---

# 3. 原理判別法の核

## 3.1 判別対象

原理判別では、少なくとも次を固定する。

```text
W = 現在の対象世界・認知世界
G = 成立させたい完成目標
P = 原理候補
[P]~ = Pと機能的に同型な構造の集合
```

ここでいう同型とは、名称・実装・外観が違っても、Pと同じ成立責任を担う構造を指す。

---

## 3.2 完全証明要求

候補Pへ、

> **Pを完全証明せよ。**

というストレステストをかける。

ただし、これはPを宇宙的・形而上的に絶対証明する要求ではない。

問うのは、

> **現在宣言したW・G・条件・射程の中で、Pなしに証明・説明・構成・運用が閉じるか。**

である。

証明手続きがPそのもの、または機能的同型構造を暗黙に必要とするなら、Pには不可欠性の証拠が生じる。

ただし、

> **証明にPが現れた／循環した**

だけでは原理判定しない。

循環は必要性の候補を示すことはあっても、原理性の十分条件ではない。

---

# 4. 除去・再導入試験

原理候補Pと、その機能的同型構造[P]~を、**隔離した検証世界**で一時的に除外する。

その上で、同一の完成目標Gを、

- 証明
- 説明
- 構成
- 実装
- 運用
- 安全確保
- 判定

しようとする。

判定は次のように分ける。

### A. PなしでGが完全に閉じる

Pは少なくとも当該W・Gでは不可欠原理ではない。

ただし「不要」「無価値」「削除可能」とまでは言わない。

### B. Pを消すとGが成立しない

Pの必要性候補が強まる。

### C. 別名・別実装で[P]~が再導入される

Pの**機能的不可避性**が強く示唆される。

### D. 判定不能

SUSPENDする。

入力不足・観測不足・同型判定不能・G未固定のまま原理認定しない。

---

# 5. 除去試験の安全境界

除去試験は、正本・本番・実環境から要素を恒久削除する操作ではない。

> **隔離した検証コピー上で行う反実仮想試験である。**

除去して挙動が変わらなかった場合も、

```text
当該条件で寄与未検出
```

と記録するに留める。

次へ飛躍してはならない。

```text
寄与未検出
→ 存在価値なし
→ 将来も不要
→ 削除可能
```

元要素、元関係、除去条件、結果、残差、反対モデルを保持する。

---

# 6. 原理判別六ゲート

完全証明要求・除去試験だけでは足りない。

候補Pは少なくとも次の六ゲートを通す。

## G1 必要性

Pまたは同型構造なしで、宣言したGが成立するか。

成立するなら、Pを不可欠原理とは呼ばない。

## G2 最小性

Pに含まれる要素のうち、さらに削っても同じ成立責任を果たせるか。

削れるなら、まだ原理核へ縮約できていない可能性がある。

## G3 代替不能性

Pを別構造Qで置き換えたとき、本当に同一Gが同一条件で閉じるか。

QがPと機能同型なら、名称違いの原理候補として扱う。

非同型のQで完全代替できるなら、P単独を不可欠原理とはしない。

## G4 生成性

Pから、複数の下流現象・規則・判断・機構・結果を説明または生成できるか。

単一事例だけを後付け説明するものを、原理へ直昇格させない。

## G5 横断性

同一の成立構造が、表面形式の異なる複数事例・複数条件でも保持されるか。

ここでいう横断性は「全学問で使える」ことを必須とする意味ではない。

**宣言した適用範囲の内部で、局所例に閉じない構造安定性を持つか**を見る。

## G6 失敗検出性

Pが成立しない条件、崩壊点、失敗署名を検出できるか。

成功だけを説明し、失敗を説明・予測・検出できない候補は弱い。

> **何を変えれば崩れるかを言えない原理候補は、成立構造をまだ掴んでいない可能性が高い。**

---

# 7. 追加監査：反対モデル・反実仮想・摂動

原理候補Pだけを見ない。

少なくとも、

- 基準モデル
- 代替モデル
- 反対仮説
- 帰無モデル
- 無変更
- 観測誤差
- 遅延効果
- 異なる目標
- 敵対条件
- 反実仮想
- 機構候補

を並列保持し得る。

Pが生成されたことを、検証済み・採用済みとみなさない。

---

# 8. 原理→原則

原理と原則を逆にしない。

```text
原理
↓
原則
```

である。

本稿では、

> **原理 = 対象・営み・体系を成立させる構造核**

> **原則 = その原理を採用した後に、運用上必然的または強く要求される条件・境界・規律**

と分ける。

例えば、ある原理から可逆性が必要と導出されるなら、

```text
可逆性を守る
```

は原理そのものではなく、その原理から導かれた原則になり得る。

原則を先に置いて、後から原理と呼び替えない。

---

# 9. 公理・定理・法則・規則との関係

名称だけで上下関係を決めない。

### 公理
体系内で出発点として採用する前提。

### 定理
公理・定義等から導出された命題。

### 法則
特定領域で安定して成立する関係・規則性の記述。

### 規則
操作・判定・運用を定める条件。

### 原則
原理採用後に導かれる運用条件・境界・規律。

### 原理
何が対象・現象・判断・体系を成立させるかという構造核。

ある「法則」が原理的構造を持つことも、ある「原理」と呼ばれるものが実際には規則・経験則・モデル内仮定であることもあり得る。

> **名称ではなく、成立責任と判別ゲートで分類する。**

---

# 10. 原理は絶対実体ではない

原理判別を通過しても、

```text
最終原理
普遍原理
不変原理
```

へ自動昇格させない。

現行体系では、

> **適用範囲付き暫定原理**

として保持する。

少なくとも、

- 時点
- 認知世界
- 主体
- 対象
- 関係
- 適用範囲
- 成立条件
- 境界
- 反証条件
- 帰還条件

を付す。

新観測により主体・対象・関係・条件・問いそのものが変われば、原理も再開放する。

---

# 11. 原理の失敗と再開放

結果が予測と合わない場合、

```text
原理が偽
```

へ直行しない。

まず、

- 対象同一性が変わった
- 適用範囲外だった
- 条件が欠けた
- 機構理解が誤っていた
- 観測方法が誤っていた
- 代替モデルが強い
- 原理候補の粒度が粗い
- 原理そのものが崩れた

を分別する。

そのうえで、

```text
維持
修正
分解
棄却
再開放
```

を行う。

---

# 12. トリニティ原理との関係

原理判別そのものも、世界・対象・関係・判定条件を必要とする。

代表的Projectionとして、

```text
X = 原理判別対象・候補P・完成目標G
R = 除去・代替・反実仮想・摂動・生成・崩壊の関係
M = 原理判定ゲート・適用範囲・反証・停止条件
```

と置ける。

ただし原理判別法をX/R/Mそのものへ還元しない。

---

# 13. 神の領域原理（仮）との関係

原理を発見したと判断しても、その原理記述を認知以前の世界本体へ昇格しない。

```text
現行条件で不可欠に見える
≠
世界本体に永遠不変の原理が刻まれている
```

である。

また、原理判別法自身も自己適用・再監査から免除しない。

---

# 14. HDSとの関係

HDS／人間意思決定理論（仮）の公開可能な機能核心として、

> **原理を見つける**

という位置づけがある。

本稿は、その「原理」という語を外部公開上で混線させないための基底定義を与える。

ただし、

- HDS内部の原理発見循環
- 内部状態
- 台帳
- ゲート実装
- 評価設計
- 判断機構
- 再現可能な運用レシピ

は本稿の公開範囲外である。

---

# 15. 原理判別の最短形

```text
原理質問
「何がこれを成立させているのか」
↓
候補P
↓
成立・関係・条件・変化・崩壊条件を記述
↓
P / [P]~ を隔離検証で除去
↓
同一Gを再構成できるか
↓
Pまたは同型構造が不可避か
↓
必要性
最小性
代替不能性
生成性
横断性
失敗検出性
↓
反対モデル・反実仮想・摂動
↓
適用範囲・反証条件・帰還条件を付与
↓
適用範囲付き暫定原理
または
SUSPEND / 再開放
```

---

# 16. 結論

原理とは、深そうな言葉でも、権威が命名した法則でもない。

> **何が、どの関係によって、どの条件で、何を成立・変化させ、何を変えれば崩れるかを説明する構造核である。**

そして原理判別は、

> **その候補を消しても同じ成立目標を閉じられるか。消した結果、結局その候補か機能同型構造を再導入せざるを得ないか。**

を問う。

ただし不可避に見えるだけでは足りない。

必要性・最小性・代替不能性・生成性・横断性・失敗検出性、反対モデル、反実仮想、摂動、反証、適用範囲を通した後にのみ、現行条件での**適用範囲付き暫定原理**として採用する。

原理もまた暫定であり、時間軸上の再開放から免れない。

---

# Part II. English Summary Projection

# What Is a Principle? / Principle Discrimination Method

**Version**: v0.1  
**Revision date**: 2026-10-07  
**Author**: がっちむち♂  
**Writing assistance**: LLM  
**Authoritative language**: Japanese  

**Translation class**: T2 / English Summary Projection  
**Source authority**: Japanese Part I / J0  
**Translation status**: CURRENT  
**Authority**: Non-authoritative and non-exhaustive. It may omit detail and must not add normative claims. In conflict, ambiguity, omission, or translation residual, Japanese Part I prevails.  
**Policy**: `TRANSLATION_POLICY.md`

## Core definition

A principle is a structural core that, under a specified time, cognitive world, subject, target, relation, and condition, explains what acts, through which relations, under which conditions, what it establishes or changes, and what must change for it to collapse.

A principle is not automatically a repeated pattern, correlation, model, mechanism, or authoritative label.

## Principle question

The basic question is:

> **What makes this possible or establishes this?**

The first answer is never privileged merely because it was first.

## Elimination and reintroduction test

Fix:

```text
W = current target/cognitive world
G = completion target
P = candidate principle
[P]~ = functionally isomorphic structures
```

Temporarily remove P and its functional equivalents in an isolated counterfactual validation copy and attempt to achieve the same G.

If G closes without P, P is not indispensable under the declared conditions. If G fails, or P/equivalent structure must be reintroduced, necessity evidence increases.

This is not a license to delete components from production or canonical records. No observed effect means only “contribution not detected under these conditions.”

## Six gates

A candidate must additionally be audited for:

1. necessity,
2. minimality,
3. non-substitutability,
4. generativity,
5. cross-case structural stability within the declared scope,
6. failure detectability.

Circularity alone is not sufficient.

## Principle → operating principle

The order is:

```text
principle
→ operating principle / rule-bound consequence
```

The underlying structural core is distinguished from downstream operational constraints derived after adopting it.

## Provisionality

A passing candidate becomes a scope-bounded provisional principle, not an immutable universal entity. Time, target identity, relations, scope, refutation conditions, and reopening conditions remain explicit.

## Relation to HDS

The public functional core of HDS includes “finding principles.” This document defines the public meaning of “principle” without disclosing internal HDS loops, gates, ledgers, or implementation recipes.
