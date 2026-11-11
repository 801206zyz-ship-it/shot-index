# -*- coding: utf-8 -*-
"""分镜 0-1 ~ 2-2"""

S01 = {
    "id": "0-1",
    "title": "茅台 vs 五粮液 2024—2025 财报分析",
    "bg": "#0b0b0d", "ink": "#f2efe6", "accent": "#c8342c", "muted": "#8b8378",
    "font": '"PingFang SC","Microsoft YaHei",sans-serif',
    "sub": "13 个镜头 · 总时长 4:06",
    "css": """
.poster{position:absolute;inset:0;background:
  radial-gradient(120% 80% at 50% 0%, #1b1a1c 0%, #0b0b0d 62%, #07070a 100%)}
.grain{position:absolute;inset:0;opacity:.28;background-image:
  repeating-linear-gradient(0deg,rgba(255,255,255,.045) 0 1px,transparent 1px 3px)}
.frame{position:absolute;inset:56px;border:3px solid rgba(232,226,210,.5)}
.frame:after{content:"";position:absolute;inset:12px;border:1px solid rgba(232,226,210,.22)}
.kick{position:absolute;left:104px;top:104px;font:600 22px/1 Consolas,monospace;
  letter-spacing:.5em;color:#c8342c}
.title{position:absolute;left:96px;top:196px;font:900 132px/1.02 "PingFang SC","Microsoft YaHei",sans-serif;
  letter-spacing:-.02em;text-shadow:0 10px 40px rgba(0,0,0,.65)}
.title em{font-style:normal;color:#c8342c}
.title .sm{display:block;font-size:44px;letter-spacing:.42em;margin-top:26px;
  color:#b9b2a4;font-weight:600}
.sub{position:absolute;left:100px;top:520px;font:500 26px/1.9 "Songti SC",serif;color:#9a9284;
  letter-spacing:.06em}
.vs{position:absolute;right:150px;top:300px;width:300px;height:300px;
  border-radius:50%;border:6px solid #c8342c;display:grid;place-items:center;
  transform:rotate(-8deg);background:rgba(200,52,44,.10)}
.vs span{font:900 116px/1 Impact,"Arial Black",sans-serif;color:#c8342c}
.vs:after{content:"";position:absolute;inset:-26px;border:2px dashed rgba(200,52,44,.42);border-radius:50%}
.nums{position:absolute;left:100px;bottom:150px;display:flex;gap:88px}
.nums div{border-left:3px solid #c8342c;padding-left:22px}
.nums b{display:block;font:900 66px/1 Impact,"Arial Black",sans-serif}
.nums i{display:block;font:500 19px/1 Consolas,monospace;color:#8b8378;
  letter-spacing:.22em;font-style:normal;margin-top:14px}
.foot{position:absolute;right:104px;bottom:66px;font:400 15px/1 Consolas,monospace;color:#6d665c;
  letter-spacing:.14em}
""",
    "body": """
<div class="poster">
  <div class="grain"></div><div class="frame"></div>
  <div class="kick fx" id="a1">FINANCIAL RATIO ANALYSIS · 2024—2025</div>
  <h1 class="title fx d1" id="a2">茅台 <em>vs</em> 五粮液<span class="sm">财 报 对 比</span></h1>
  <div class="sub fx d2" id="a3">十项比率 · 两年对照 · 两次口径变更之后<br>贵州茅台 600519.SH　｜　五粮液 000858.SZ</div>
  <div class="vs fx" id="a4"><span>VS</span></div>
  <div class="nums">
    <div class="fx" id="a5"><b id="n1">0</b><i>CAMERA SHOTS</i></div>
    <div class="fx d1" id="a6"><b id="n2">0</b><i>CHAPTERS</i></div>
    <div class="fx d2" id="a7"><b id="n3">0</b><i>RATIOS</i></div>
  </div>
  <div class="foot fx d3" id="a8">数据：两家公司 2024 / 2025 年度报告（合并报表口径）</div>
</div>
""",
    "cues": [
        {"t": 300, "sel": "#a1", "act": "on"},
        {"t": 600, "sel": "#a2", "act": "on"},
        {"t": 1400, "sel": "#a3", "act": "on"},
        {"t": 2200, "sel": "#a4", "act": "on"},
        {"t": 2800, "sel": "#a5", "act": "on"},
        {"t": 2900, "sel": "#n1", "act": "count", "arg": 13},
        {"t": 3050, "sel": "#a6", "act": "on"},
        {"t": 3150, "sel": "#n2", "act": "count", "arg": 5},
        {"t": 3300, "sel": "#a7", "act": "on"},
        {"t": 3400, "sel": "#n3", "act": "count", "arg": 10},
        {"t": 3900, "sel": "#a8", "act": "on"},
    ],
    "dur": 22,
}

S11 = {
    "id": "1-1",
    "title": "两家公司是谁：企业背景双雄档案",
    "bg": "#cfc4ab", "ink": "#2b2620", "accent": "#8c2f22", "muted": "#6b6252",
    "font": '"Songti SC","SimSun",serif',
    "sub": "档案卷宗 · 2025 年年报口径",
    "css": """
.desk{position:absolute;inset:0;background:
  radial-gradient(120% 90% at 20% 10%, #ded3ba 0%, #cfc4ab 55%, #b9ad94 100%)}
.desk:after{content:"";position:absolute;inset:0;opacity:.35;
  background-image:repeating-linear-gradient(0deg,rgba(90,78,58,.10) 0 1px,transparent 1px 4px)}
.head{position:absolute;left:96px;top:74px;font:600 20px/1 Consolas,monospace;
  letter-spacing:.42em;color:#7a6d57}
.h1{position:absolute;left:94px;top:112px;font:700 62px/1.1 "Songti SC",serif;letter-spacing:.02em}
.folder{position:absolute;top:250px;width:700px;height:600px;background:#e7dcc0;
  box-shadow:0 18px 40px rgba(60,48,30,.28);border:1px solid #c6b795}
.folder.l{left:96px;transform:rotate(-1.2deg)}
.folder.r{right:96px;transform:rotate(1deg)}
.tab{position:absolute;top:-46px;left:38px;padding:10px 30px 12px;font:600 20px/1 Consolas,monospace;
  letter-spacing:.2em;color:#f6efe0}
.tab.l{background:#8c2f22}.tab.r{background:#2f4f5f}
.fhead{position:absolute;left:38px;top:34px;font:700 42px/1.2 "Songti SC",serif}
.fcode{position:absolute;left:40px;top:92px;font:500 19px/1 Consolas,monospace;letter-spacing:.18em;color:#6b6252}
.rule{position:absolute;left:38px;right:38px;top:130px;height:2px;background:#b9a980}
.rows{position:absolute;left:38px;right:38px;top:158px}
.row{display:flex;justify-content:space-between;align-items:baseline;padding:16px 0;
  border-bottom:1px dashed #c2b18d}
.row span{font:500 21px/1 "Songti SC",serif;color:#5d5442}
.row b{font:700 40px/1 Consolas,monospace;letter-spacing:-.01em}
.row em{font-style:normal;font-size:20px;color:#8c2f22;margin-left:6px;font-family:"Songti SC",serif}
.stamp{position:absolute;right:30px;bottom:26px;width:132px;height:132px;border:3px solid rgba(140,47,34,.55);
  border-radius:50%;display:grid;place-items:center;transform:rotate(-14deg);color:rgba(140,47,34,.65);
  font:700 15px/1.5 Consolas,monospace;letter-spacing:.12em;text-align:center}
.foot{position:absolute;left:96px;bottom:56px;font:500 16px/1 Consolas,monospace;color:#6b6252;letter-spacing:.1em}
""",
    "body": """
<div class="desk">
  <div class="head fx" id="b1">ARCHIVE · 2025 ANNUAL REPORT</div>
  <div class="h1 fx d1" id="b2">两家公司是谁</div>
  <div class="folder l fx d2" id="b3">
    <div class="tab l">贵州茅台</div>
    <div class="fhead">贵州茅台酒</div>
    <div class="fcode">600519.SH · 上交所主板 · 贵州仁怀</div>
    <div class="rule"></div>
    <div class="rows">
      <div class="row"><span>营业收入</span><b id="m1">0</b><em>亿元</em></div>
      <div class="row"><span>归母净利润</span><b id="m2">0</b><em>亿元</em></div>
      <div class="row"><span>毛利率</span><b id="m3">0</b><em>%</em></div>
      <div class="row"><span>资产负债率</span><b id="m4">0</b><em>%</em></div>
    </div>
    <div class="stamp">合并报表<br>2025 年度</div>
  </div>
  <div class="folder r fx d3" id="b4">
    <div class="tab r">五粮液</div>
    <div class="fhead">宜宾五粮液</div>
    <div class="fcode">000858.SZ · 深交所主板 · 四川宜宾</div>
    <div class="rule"></div>
    <div class="rows">
      <div class="row"><span>营业收入</span><b id="w1">0</b><em>亿元</em></div>
      <div class="row"><span>归母净利润</span><b id="w2">0</b><em>亿元</em></div>
      <div class="row"><span>毛利率</span><b id="w3">0</b><em>%</em></div>
      <div class="row"><span>资产负债率</span><b id="w4">0</b><em>%</em></div>
    </div>
    <div class="stamp" style="border-color:rgba(47,79,95,.55);color:rgba(47,79,95,.7)">合并报表<br>2025 年度</div>
  </div>
  <div class="foot fx d3" id="b5">数据来源：两家公司 2025 年年度报告（合并报表口径）</div>
</div>
""",
    "cues": [
        {"t": 200, "sel": "#b1", "act": "on"},
        {"t": 500, "sel": "#b2", "act": "on"},
        {"t": 900, "sel": "#b3", "act": "on"},
        {"t": 1500, "sel": "#m1", "act": "count", "arg": 1688.38, "dec": 2},
        {"t": 1900, "sel": "#m2", "act": "count", "arg": 823.20, "dec": 2},
        {"t": 2300, "sel": "#m3", "act": "count", "arg": 91.18, "dec": 2},
        {"t": 2700, "sel": "#m4", "act": "count", "arg": 16.42, "dec": 2},
        {"t": 3400, "sel": "#b4", "act": "on"},
        {"t": 4000, "sel": "#w1", "act": "count", "arg": 405.29, "dec": 2},
        {"t": 4400, "sel": "#w2", "act": "count", "arg": 89.54, "dec": 2},
        {"t": 4800, "sel": "#w3", "act": "count", "arg": 77.54, "dec": 2},
        {"t": 5200, "sel": "#w4", "act": "count", "arg": 35.69, "dec": 2},
        {"t": 6200, "sel": "#b5", "act": "on"},
    ],
    "dur": 18,
}

S21 = {
    "id": "2-1",
    "title": "资产负债表：一个高现金，一个扩产加预收",
    "bg": "#101a16", "ink": "#eee6d2", "accent": "#c9a227", "muted": "#8d9584",
    "font": '"Songti SC","SimSun",serif',
    "sub": "黄铜天平 · 资产与负债的两端",
    "css": """
.brass{position:absolute;inset:0;background:
  radial-gradient(90% 70% at 50% 0%, #1b2a23 0%, #101a16 60%, #0a1210 100%)}
.kick{position:absolute;left:96px;top:82px;font:600 20px/1 Consolas,monospace;letter-spacing:.4em;color:#c9a227}
.h1{position:absolute;left:94px;top:120px;font:700 58px/1.15 "Songti SC",serif;color:#eee6d2}
.scale{position:absolute;left:50%;top:268px;width:1200px;margin-left:-600px;height:520px}
.post{position:absolute;left:588px;top:60px;width:24px;height:400px;background:linear-gradient(90deg,#7a5f18,#d9b23c 45%,#7a5f18)}
.base{position:absolute;left:430px;top:452px;width:340px;height:16px;background:linear-gradient(90deg,#7a5f18,#d9b23c,#7a5f18);
  border-radius:8px}
.arm{position:absolute;left:120px;top:58px;width:960px;height:12px;border-radius:6px;
  background:linear-gradient(90deg,#7a5f18,#e6c258 50%,#7a5f18);transform-origin:50% 50%;
  transition:transform 1.4s cubic-bezier(.2,.8,.2,1)}
.arm.tilt{transform:rotate(7.6deg)}
.pan{position:absolute;top:120px;width:400px;text-align:center;transition:transform 1.4s cubic-bezier(.2,.8,.2,1)}
.pan.a{left:20px}.pan.b{right:20px}
.pan.a.drop{transform:translateY(64px)}
.pan .line{width:2px;height:70px;margin:0 auto;background:#b8942a}
.pan .dish{width:400px;height:22px;border-radius:0 0 200px 200px;background:linear-gradient(180deg,#d9b23c,#8a6a1a)}
.pan .big{font:900 84px/1 Impact,"Arial Black",sans-serif;color:#f4ea4a;letter-spacing:-.02em;
  margin-top:-14px}
.pan .cap{font:500 22px/1.6 "Songti SC",serif;color:#b9bfae;margin-top:10px}
.pan .tag{display:inline-block;margin-top:16px;padding:8px 18px;border:1px solid rgba(201,162,39,.6);
  font:600 18px/1 Consolas,monospace;letter-spacing:.16em;color:#c9a227}
.legend{position:absolute;left:96px;bottom:120px;font:500 21px/2 "Songti SC",serif;color:#9aa392}
.legend b{color:#f4ea4a;font-family:Consolas,monospace}
.foot{position:absolute;right:96px;bottom:66px;font:400 15px/1 Consolas,monospace;color:#6f7a6b;letter-spacing:.1em}
""",
    "body": """
<div class="brass">
  <div class="kick fx" id="c1">BALANCE SHEET · 2025</div>
  <div class="h1 fx d1" id="c2">一个高现金，一个扩产加预收</div>
  <div class="scale">
    <div class="post fx d2" id="c3"></div>
    <div class="base fx d2" id="c4"></div>
    <div class="arm" id="arm"></div>
    <div class="pan a" id="panA">
      <div class="line"></div><div class="dish"></div>
      <div class="big" id="k1">0</div>
      <div class="cap">流动比率<br>流动资产 ÷ 流动负债</div>
      <div class="tag">茅台 5.09×</div>
    </div>
    <div class="pan b" id="panB">
      <div class="line"></div><div class="dish"></div>
      <div class="big" id="k2">0</div>
      <div class="cap">流动比率<br>流动资产 ÷ 流动负债</div>
      <div class="tag">五粮液 2.45×</div>
    </div>
  </div>
  <div class="legend fx d3" id="c5">资产总计：茅台 <b>3,038.35</b> 亿元　｜　五粮液 <b>1,899.84</b> 亿元<br>
  负债合计：茅台 <b>498.76</b> 亿元　｜　五粮液 <b>678.04</b> 亿元</div>
  <div class="foot fx d3" id="c6">数据：2025 年年度报告（合并报表口径）</div>
</div>
""",
    "cues": [
        {"t": 200, "sel": "#c1", "act": "on"},
        {"t": 500, "sel": "#c2", "act": "on"},
        {"t": 900, "sel": "#c3", "act": "on"},
        {"t": 1050, "sel": "#c4", "act": "on"},
        {"t": 1500, "sel": "#k1", "act": "count", "arg": 5.09, "dec": 2},
        {"t": 1900, "sel": "#k2", "act": "count", "arg": 2.45, "dec": 2},
        {"t": 2600, "sel": "#panA", "act": "cls", "arg": "drop"},
        {"t": 2750, "sel": "#arm", "act": "cls", "arg": "tilt"},
        {"t": 3800, "sel": "#c5", "act": "on"},
        {"t": 4600, "sel": "#c6", "act": "on"},
    ],
    "dur": 18,
}

S22 = {
    "id": "2-2",
    "title": "利润表：营收腰斩 54.5% 的那一年",
    "bg": "#efe7d6", "ink": "#241f1a", "accent": "#8f1d13", "muted": "#6a6258",
    "font": '"Songti SC","SimSun",serif',
    "sub": "复古报纸 · 第 2 版 · 财经头条",
    "css": """
.paper{position:absolute;inset:0;background:
  radial-gradient(120% 100% at 30% 0%, #f7f0e1 0%, #efe7d6 60%, #ddd2bd 100%)}
.paper:after{content:"";position:absolute;inset:0;opacity:.4;
  background-image:repeating-linear-gradient(90deg,rgba(120,105,80,.06) 0 1px,transparent 1px 5px)}
.mast{position:absolute;left:80px;right:80px;top:52px;border-bottom:4px double #241f1a;padding-bottom:14px;
  display:flex;justify-content:space-between;align-items:flex-end;
  font:600 18px/1 Consolas,monospace;letter-spacing:.3em;color:#5b5348}
.mast b{font:700 26px/1 "Songti SC",serif;letter-spacing:.5em}
.headline{position:absolute;left:80px;right:80px;top:140px;font:900 128px/1.02 "Songti SC",serif;
  letter-spacing:-.01em;color:#241f1a}
.headline em{font-style:normal;color:#8f1d13}
.deck{position:absolute;left:84px;right:84px;top:300px;font:500 30px/1.7 "Songti SC",serif;color:#4a433a}
.cols{position:absolute;left:84px;right:84px;top:404px;column-count:3;column-gap:52px;
  font:400 20px/1.95 "Songti SC",serif;color:#3b352d;text-align:justify}
.cols p{margin-bottom:14px}
.drop{float:left;font:700 76px/0.9 "Songti SC",serif;color:#8f1d13;padding:6px 12px 0 0}
.inset{position:absolute;left:84px;right:84px;top:592px;border:2px solid #8f1d13;padding:20px 28px;\n  font:500 26px/1.6 "Songti SC",serif;color:#3b352d;background:rgba(143,29,19,.05)}\n.inset em{font-style:normal;color:#8f1d13;font-weight:700}\n.kpirow{position:absolute;left:84px;right:84px;bottom:118px;display:flex;gap:26px}
.kpi{flex:1;border-top:3px solid #8f1d13;padding-top:16px}
.kpi b{display:block;font:900 58px/1 Impact,"Arial Black",sans-serif;color:#8f1d13;letter-spacing:-.01em}
.kpi span{display:block;margin-top:10px;font:500 18px/1.5 "Songti SC",serif;color:#5b5348}
.foot{position:absolute;left:84px;bottom:64px;font:500 15px/1 Consolas,monospace;color:#6a6258;letter-spacing:.12em}
""",
    "body": """
<div class="paper">
  <div class="mast fx" id="d1"><b>财经年报</b><span>2026 · 05 · 第 2 版</span></div>
  <div class="headline fx d1" id="d2">营收腰斩 <em>54.5%</em></div>
  <div class="deck fx d2" id="d3">五粮液 2025 年营业收入 405.29 亿元，为近十年最低；归母净利润 89.54 亿元，同比 −71.89%。</div>
  <div class="cols fx d3" id="d4">
    <p><span class="drop">2</span>026 年 4 月 30 日深夜，五粮液发布《关于前期会计差错更正的公告》，将收入确认由「发货给经销商」改为「货到终端」。</p>
    <p>前三季度营业收入由 609.45 亿元追溯调减至 306.38 亿元，一次性抹掉 303.08 亿元；全年营收因此定格在 405.29 亿元。</p>
    <p>同期茅台营业收入 1,688.38 亿元，同比仅 −1.21%，为 2001 年上市以来首次下滑。</p>
  </div>
  <div class="inset fx d3" id="d7">公告原话：「公司对收入确认时点进行了重新判断，<em>由发货确认改为终端销售确认</em>。」—— 一句话，303 亿元收入移到下一年。</div>\n  <div class="kpirow fx d3" id="d5">
    <div class="kpi"><b id="e1">0</b><span>五粮液营收（亿元）</span></div>
    <div class="kpi"><b id="e2">0</b><span>营收同比（%）</span></div>
    <div class="kpi"><b id="e3">0</b><span>归母净利同比（%）</span></div>
    <div class="kpi"><b id="e4">0</b><span>被追溯调减（亿元）</span></div>
  </div>
  <div class="foot fx d3" id="d6">数据：五粮液《关于前期会计差错更正的公告》（2026-04-30）、2025 年年度报告</div>
</div>
""",
    "cues": [
        {"t": 200, "sel": "#d1", "act": "on"},
        {"t": 500, "sel": "#d2", "act": "on"},
        {"t": 1300, "sel": "#d3", "act": "on"},
        {"t": 2200, "sel": "#d4", "act": "on"},
        {"t": 3300, "sel": "#d7", "act": "on"},
        {"t": 3700, "sel": "#d5", "act": "on"},
        {"t": 3800, "sel": "#e1", "act": "count", "arg": 405.29, "dec": 2},
        {"t": 4300, "sel": "#e2", "act": "count", "arg": -54.55, "dec": 2},
        {"t": 4800, "sel": "#e3", "act": "count", "arg": -71.89, "dec": 2},
        {"t": 5300, "sel": "#e4", "act": "count", "arg": 303.08, "dec": 2},
        {"t": 6400, "sel": "#d6", "act": "on"},
    ],
    "dur": 20,
}

SHOTS = [S01, S11, S21, S22]
