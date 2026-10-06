# 原理とは何か／原理判別法
## ― 観測・パターン・モデル・機構を原理へ誤昇格させないための認知工学的判別仕様 ―

**版**：v0.2  
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

## 3.1 判定の核心

原理候補Pに対して、**数学の完全証明を当てる。**

ここでいう「数学の完全証明」とは、単に

> Pをもっともらしく説明せよ

という意味ではない。

命題Pを、採用した公理・定義・前提・関係から完全に証明する方向へ展開し、

> **その証明構造が、最終的にP自身またはPと機能同型の構造へ再帰・再起・回帰するか**

を観測する。

最短形は次である。

```text
命題P
↓
数学の完全証明を当てる
↓
証明を完全展開する
↓
P自身または機能同型構造へ戻るか
↓
YES → 原理候補
NO  → 上位構造から導出された派生命題・定理・規則等として再分類
```

この**再帰性**が原理判別法の主判定である。

---

## 3.2 再帰と循環論法を分ける

ここでいう再帰は、

```text
Pは正しい
なぜならPだから
```

という論証上の循環論法ではない。

そうではなく、

```text
Pを証明する
↓
証明の依存関係を展開する
↓
上位条件・関係・構造へ遡る
↓
証明を閉じようとする
↓
PまたはPと機能同型の構造が再び必要になる
```

という**構造的回帰**を指す。

したがって判定対象は、文章上同じ語が再登場したかではない。

> **同じ成立責任を持つ構造が、証明を閉じるために不可避に再出現するか。**

を見る。

---

## 3.3 原理候補・派生構造の分別

数学の完全証明を当てた結果、

### A. P自身へ再帰する

Pは原理候補として強く残る。

### B. Pと機能同型の構造へ再帰する

名称・表現が違っても、Pの構造核が再帰したとみなし、原理候補として扱う。

### C. Pへ戻らず、別の上位構造Qで証明が閉じる

PはQから導出される派生命題・定理・規則・モデル内結果等として再分類する。

### D. 回帰先がさらに下位の局所構造である

Pを普遍原理へ昇格せず、**派生原理・局所原理候補**として適用範囲を限定する。

### E. 証明条件自体が閉じない

SUSPENDする。

---

# 4. 数学の完全証明を当てる意味

原理判別法で数学を使う理由は、数式へ変換すれば偉いからではない。

> **前提、定義、関係、導出、依存、完了条件を省略せず、どこへ回帰するかを追跡するため**

である。

したがって数学の完全証明は、

- 記号化
- 形式化
- 公理化
- 定義展開
- 依存関係展開
- 反証可能な完了条件

を用いてよいが、形式のための形式化を目的にしない。

重要なのは、

```text
証明の終点がどこか
証明が何を再要求するか
何へ再帰するか
```

である。

---

# 5. 補助監査：除去・同型再導入試験

数学の完全証明による再帰判定を補強するため、必要に応じて原理候補Pとその機能同型構造[P]~を隔離検証上で一時的に除外する。

その上で同じ成立目標Gを再構成する。

```text
P / [P]~ を除外
↓
同一Gを再構成
↓
Pまたは同型構造が再導入されるか
```

この試験は、**完全証明で観測された再帰を別角度から確認する補助監査**であり、原理判別の主判定そのものではない。

除去試験は正本・本番・実環境から要素を恒久削除する操作ではない。

> **隔離した検証コピー上で行う反実仮想試験である。**

除去して挙動が変わらなかった場合も、

```text
当該条件で寄与未検出
```

と記録するに留める。

---

# 6. 再帰後の監査

再帰しただけで、その適用範囲・粒度まで自動確定したとは扱わない。

再帰が観測された原理候補について、少なくとも次を補助監査する。

## G1 最小性
再帰している構造から、さらに削れる余剰要素がないか。

## G2 同型性
表面語ではなく、成立責任が本当に同じ構造へ回帰しているか。

## G3 生成性
その構造から複数の下流現象・規則・判断・機構を導出できるか。

## G4 横断性
宣言した適用範囲の中で、局所一例だけでなく同型の再帰が保持されるか。

## G5 失敗検出性
その原理が成立しない条件・崩壊点・失敗署名を示せるか。

## G6 適用範囲
普遍原理なのか、派生原理なのか、局所原理なのかを区別できるか。

これらは**再帰判定の後段監査**であり、

```text
数学の完全証明
→ 再帰するか
```

という原理判別の核心を置き換えない。

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
命題・原理候補P
↓
Pに数学の完全証明を当てる
↓
証明を最後まで展開する
↓
P自身または機能同型構造へ
自己循環・再起・回帰するか
↓
YES
→ 原理候補
→ 回帰先と適用範囲を分類
→ 最小性・同型性・生成性・横断性・失敗検出性を補助監査
→ 適用範囲付き暫定原理

NO
→ 上位構造から導出される
  定理・規則・モデル内結果等へ再分類

判定不能
→ SUSPEND
```

---

# 16. 結論

原理とは、深そうな言葉でも、権威が命名した法則でもない。

> **何が、どの関係によって、どの条件で、何を成立・変化させ、何を変えれば崩れるかを説明する構造核である。**

そして原理判別の核心は、

> **命題に数学の完全証明を当て、その証明構造が命題自身または機能同型構造へ自己循環・再起・回帰するかを見ること。**

である。

再帰した候補は原理候補として残し、その後に最小性・同型性・生成性・横断性・失敗検出性・適用範囲を監査する。

再帰せず別の上位構造から証明が閉じるなら、定理・規則・派生命題等へ再分類する。

原理もまた暫定であり、時間軸上の再開放から免れない。

---

# Part II. English Summary Projection

# What Is a Principle? / Principle Discrimination Method

**Version**: v0.2  
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

## Core discrimination test

Apply a **complete mathematical proof** to candidate proposition P and fully expand its proof dependencies.

The primary question is:

> **Does the completed proof recursively return to P itself, or to a functionally isomorphic structure carrying the same establishment responsibility?**

```text
P
→ complete mathematical proof
→ fully expand dependencies
→ recursive return / reactivation / recurrence?
```

If yes, P remains a principle candidate. If the proof closes through a distinct higher-order structure without returning to P or an isomorphic structure, P is reclassified as a derived theorem, rule, model-internal result, or other downstream structure.

This structural recursion is not the trivial circular argument “P because P.” It is the reappearance of the same functional structure as a necessary condition for closing the proof.

## Secondary audits

Elimination and functional reintroduction tests may be used as supporting counterfactual audits after the recursion test. They do not replace the core criterion.

After recursion is observed, minimality, isomorphism, generativity, cross-case stability, failure detectability, and scope are audited before adopting a scope-bounded provisional principle.

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
