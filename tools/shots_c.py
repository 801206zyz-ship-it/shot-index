# -*- coding: utf-8 -*-
"""3-4 ~ 4-1 五个镜头。几何全部静态渲染，只做淡入与数字滚动。"""

SANS = '"PingFang SC","Microsoft YaHei",sans-serif'
MONO = 'Consolas,"Courier New",monospace'

S34 = {
    "id": "3-4",
    "title": "偿债能力：负债率 19.64% 与 55.49%",
    "dur": 18,
    "bg": "#060d0b",
    "ink": "#e3f6ea",
    "accent": "#5ef0a8",
    "muted": "#72928621",
    "font": SANS,
    "sub": "3-4 · 双环荧光仪表 · 12,177",
    "css": """
.gauge{position:absolute;inset:0;
  background:radial-gradient(70% 60% at 50% 108%,#0e3a28 0%,#08201a 45%,#060d0b 78%)}
.kick{position:absolute;left:96px;top:82px;font:700 19px/1 Consolas,monospace;letter-spacing:.42em;color:#5ef0a8}
.h1{position:absolute;left:94px;top:118px;font:700 76px/1.16 "__FONT__";letter-spacing:.01em}
.h1 em{font-style:normal;color:#5ef0a8}
.rings{position:absolute;left:0;right:0;top:300px;height:420px;display:flex;justify-content:center;
  gap:190px;align-items:flex-start}
.ring{position:relative;width:340px;height:340px}
.ring svg{position:absolute;inset:0;transform:rotate(-90deg)}
.ring .bgc{fill:none;stroke:rgba(94,240,168,.13);stroke-width:16}
.ring .fg{fill:none;stroke:#5ef0a8;stroke-width:16;stroke-linecap:round}
.ring b{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;
  font:700 74px/1 Consolas,monospace;letter-spacing:-.02em}
.ring b i{font-style:normal;font-size:30px;margin-left:6px;color:#8fd8b4}
.ring .lab{position:absolute;left:0;right:0;top:368px;text-align:center;
  font:600 22px/1.5 "__FONT__";color:#9fc4b0}
.ring .who{position:absolute;left:0;right:0;top:-46px;text-align:center;
  font:700 24px/1 "__FONT__";letter-spacing:.06em}
.ring.a .who{color:#5ef0a8}.ring.b .who{color:#ff9f43}
.ring.b .fg{stroke:#ff9f43}.ring.b .bgc{stroke:rgba(255,159,67,.14)}
.ring.b b i{color:#e0b184}
.bar2{position:absolute;left:150px;right:150px;bottom:196px;height:1px;background:rgba(94,240,168,.22)}
.note{position:absolute;left:96px;bottom:150px;font:400 21px/1.9 "__FONT__";color:#8aa79a}
.note b{color:#5ef0a8;font-family:Consolas,monospace}
.foot{position:absolute;right:96px;bottom:150px;text-align:right;
  font:400 15px/1.8 Consolas,monospace;color:#4f6f60;letter-spacing:.08em}
""",
    "body": """
<div class="gauge">
  <div class="kick fx" id="c1">SOLVENCY · 2025</div>
  <div class="h1 fx d1" id="c2">谁在<em>借杠杆</em>，谁在<em>收杠杆</em></div>
  <div class="rings">
    <div class="ring a fx d2" id="c3">
      <div class="who">贵州茅台</div>
      <svg viewBox="0 0 340 340">
        <circle class="bgc" cx="170" cy="170" r="150"></circle>
        <circle class="fg" cx="170" cy="170" r="150"
          stroke-dasharray="942.5" stroke-dashoffset="757.5"></circle>
      </svg>
      <b><span id="na">0</span><i>%</i></b>
      <div class="lab">资产负债率 · 负债 4,987,559 / 资产 30,383,484（万元）</div>
    </div>
    <div class="ring b fx d3" id="c4">
      <div class="who">五粮液</div>
      <svg viewBox="0 0 340 340">
        <circle class="bgc" cx="170" cy="170" r="150"></circle>
        <circle class="fg" cx="170" cy="170" r="150"
          stroke-dasharray="942.5" stroke-dashoffset="419.4"></circle>
      </svg>
      <b><span id="nb">0</span><i>%</i></b>
      <div class="lab">资产负债率 · 负债 6,780,359 / 资产 18,998,427（万元）</div>
    </div>
  </div>
  <div class="note fx" id="c5"><b>19.64%</b> 与 <b>55.49%</b>，相差 35.85 个百分点。<br>
    两家都没有有息负债，比率高低反映的是<b>经营性占款</b>的多少，而非偿债风险。</div>
  <div class="foot">数据：2025 年报（合并口径）</div>
</div>
""",
    "cues": [
        {"t": 200, "sel": "#c1", "act": "on"},
        {"t": 500, "sel": "#c2", "act": "on"},
        {"t": 1000, "sel": "#c3", "act": "on"},
        {"t": 1150, "sel": "#c4", "act": "on"},
        {"t": 1700, "sel": "#na", "act": "count", "arg": 19.64, "dec": 2},
        {"t": 1850, "sel": "#nb", "act": "count", "arg": 55.49, "dec": 2},
        {"t": 3200, "sel": "#c5", "act": "on"},
    ],
}

S35 = {
    "id": "3-5",
    "title": "周转率：1419 天与 768 天",
    "dur": 18,
    "bg": "#f2ead8",
    "ink": "#22201c",
    "accent": "#c2410c",
    "muted": "#8a8070",
    "font": SANS,
    "sub": "3-5 · 横向跑道速度条 · 16,640",
    "css": """
.track{position:absolute;inset:0;background:
  radial-gradient(120% 90% at 50% 0%,#f7f0e0 0%,#f2ead8 55%,#e8dfc9 100%)}
.kick{position:absolute;left:96px;top:80px;font:700 19px/1 Consolas,monospace;letter-spacing:.4em;color:#c2410c}
.h1{position:absolute;left:94px;top:116px;font:700 74px/1.16 "__FONT__"}
.h1 em{font-style:normal;color:#c2410c}
.lanes{position:absolute;left:96px;right:96px;top:300px}
.lane{position:relative;height:96px;margin-bottom:26px}
.lane .nm{position:absolute;left:0;top:26px;width:250px;font:700 24px/1 "__FONT__"}
.lane .tr{position:absolute;left:270px;right:250px;top:40px;height:26px;
  background:rgba(34,32,28,.08);border-radius:13px;overflow:hidden}
.lane .fl{height:100%;border-radius:13px;background:linear-gradient(90deg,#e2721f,#c2410c)}
.lane.b .fl{background:linear-gradient(90deg,#7a8f4a,#4d5f2a)}
.lane .vl{position:absolute;right:8px;top:14px;text-align:right;font:700 34px/1 Consolas,monospace;color:#22201c}
.lane .sub{position:absolute;left:270px;top:74px;font:400 15px/1 Consolas,monospace;color:#8a8070}
.mid{position:absolute;left:96px;right:96px;top:770px;height:1px;background:rgba(34,32,28,.18)}
.note{position:absolute;left:96px;top:800px;font:400 21px/1.85 "__FONT__";color:#4a463d;max-width:1200px}
.note b{color:#c2410c;font-family:Consolas,monospace}
.foot{position:absolute;right:96px;bottom:52px;font:400 15px/1 Consolas,monospace;color:#8a8070;letter-spacing:.08em}
""",
    "body": """
<div class="track">
  <div class="kick fx" id="d1">TURNOVER · 2025</div>
  <div class="h1 fx d1" id="d2">同一个行业，<em>两种节奏</em></div>
  <div class="lanes">
    <div class="lane a fx d2" id="d3"><div class="nm">茅台 · 2025</div>
      <div class="tr"><div class="fl" style="width:100%"></div></div>
      <div class="vl"><span id="ta">0</span> 天</div>
      <div class="sub">存货周转率 0.26 次 · 存货 6,142,742 万元</div></div>
    <div class="lane a fx d2" id="d4"><div class="nm">茅台 · 2024</div>
      <div class="tr"><div class="fl" style="width:94%"></div></div>
      <div class="vl"><span id="tb">0</span> 天</div>
      <div class="sub">存货周转率 0.27 次 · 存货 5,434,329 万元</div></div>
    <div class="lane b fx d3" id="d5"><div class="nm">五粮液 · 2025</div>
      <div class="tr"><div class="fl" style="width:54%"></div></div>
      <div class="vl"><span id="tc">0</span> 天</div>
      <div class="sub">存货周转率 0.48 次 · 存货 2,006,534 万元</div></div>
    <div class="lane b fx d3" id="d6"><div class="nm">五粮液 · 2024</div>
      <div class="tr"><div class="fl" style="width:22%"></div></div>
      <div class="vl"><span id="td">0</span> 天</div>
      <div class="sub">存货周转率 1.15 次 · 存货 1,823,370 万元</div></div>
  </div>
  <div class="mid"></div>
  <div class="note fx" id="d7">茅台 1,419 天里有 4 年是<b>基酒陈酿</b>，慢是工艺；五粮液一年之内从 317 天走成 768 天，
    是<b>货压在仓里</b>。两条跑道，读法完全不同。</div>
  <div class="foot">数据：2024 / 2025 年报（合并口径）</div>
</div>
""",
    "cues": [
        {"t": 200, "sel": "#d1", "act": "on"},
        {"t": 500, "sel": "#d2", "act": "on"},
        {"t": 900, "sel": "#d3", "act": "on"},
        {"t": 1050, "sel": "#d4", "act": "on"},
        {"t": 1700, "sel": "#d5", "act": "on"},
        {"t": 1850, "sel": "#d6", "act": "on"},
        {"t": 1300, "sel": "#ta", "act": "count", "arg": 1419},
        {"t": 1450, "sel": "#tb", "act": "count", "arg": 1334},
        {"t": 2100, "sel": "#tc", "act": "count", "arg": 768},
        {"t": 2250, "sel": "#td", "act": "count", "arg": 317},
        {"t": 3600, "sel": "#d7", "act": "on"},
    ],
}

S36 = {
    "id": "3-6",
    "title": "茅台 2025：从 2200 元到 1399 元",
    "dur": 20,
    "bg": "#0a0a0c",
    "ink": "#f0ece4",
    "accent": "#ff3b30",
    "muted": "#6d6a64",
    "font": SANS,
    "sub": "3-6 · 折线下坠曲线 · 20,088",
    "css": """
.slide{position:absolute;inset:0;background:
  radial-gradient(90% 70% at 78% 6%,#2a0a0a 0%,#120607 42%,#0a0a0c 80%)}
.kick{position:absolute;left:96px;top:80px;font:700 19px/1 Consolas,monospace;letter-spacing:.4em;color:#ff3b30}
.h1{position:absolute;left:94px;top:116px;font:700 72px/1.18 "__FONT__"}
.h1 em{font-style:normal;color:#ff3b30}
.chartbox{position:absolute;left:96px;right:96px;top:330px;height:470px}
.chartbox svg{width:100%;height:100%;overflow:visible}
.grid{stroke:rgba(240,236,228,.10);stroke-width:1}
.axis{stroke:rgba(240,236,228,.28);stroke-width:2}
.pl{fill:none;stroke:#ff3b30;stroke-width:5;stroke-linejoin:round;stroke-linecap:round}
.dot{fill:#0a0a0c;stroke:#ff3b30;stroke-width:4}
.tag{position:absolute;font:700 20px/1 Consolas,monospace;color:#ff6b62;white-space:nowrap}
.tag.w{color:#f0ece4}
.xlab{position:absolute;top:486px;font:400 15px/1 Consolas,monospace;color:#8b8781;letter-spacing:.06em}
.kpi{position:absolute;top:150px;right:96px;text-align:right}
.kpi div{font:400 15px/1 Consolas,monospace;color:#8b8781;letter-spacing:.16em;margin-bottom:12px}
.kpi b{display:block;font:700 62px/1 Consolas,monospace;color:#ff3b30;letter-spacing:-.02em}
.kpi b.s{font-size:34px;color:#f0ece4;margin-top:8px}
.note{position:absolute;left:96px;bottom:70px;font:400 21px/1.8 "__FONT__";color:#b9b3a8;max-width:1180px}
.note b{color:#ff6b62}
""",
    "body": """
<div class="slide">
  <div class="kick fx" id="e1">PRICE PATH · 2025</div>
  <div class="h1 fx d1" id="e2">飞天批价，<em>一年跌掉三分之一</em></div>
  <div class="kpi fx d2" id="e3"><div>2025 年初 → 双 11</div>
    <b>2,200 → 1,399</b><b class="s">−36.4%</b></div>
  <div class="chartbox fx d2" id="e4">
    <svg viewBox="0 0 1600 470" preserveAspectRatio="none">
      <line class="grid" x1="0" y1="60" x2="1600" y2="60"></line>
      <line class="grid" x1="0" y1="170" x2="1600" y2="170"></line>
      <line class="grid" x1="0" y1="280" x2="1600" y2="280"></line>
      <line class="grid" x1="0" y1="390" x2="1600" y2="390"></line>
      <line class="axis" x1="0" y1="440" x2="1600" y2="440"></line>
      <polyline class="pl" points="40,48 300,132 560,214 820,286 1080,352 1340,398 1520,404"></polyline>
      <circle class="dot" cx="40" cy="48" r="9"></circle>
      <circle class="dot" cx="560" cy="214" r="9"></circle>
      <circle class="dot" cx="1080" cy="352" r="9"></circle>
      <circle class="dot" cx="1520" cy="404" r="9"></circle>
    </svg>
    <div class="tag w" style="left:24px;top:0">2,200</div>
    <div class="tag" style="left:500px;top:166px">1,700</div>
    <div class="tag" style="left:1010px;top:300px">1,499 指导价</div>
    <div class="tag" style="left:1380px;top:352px">1,399</div>
    <div class="xlab" style="left:20px">01 月</div>
    <div class="xlab" style="left:330px">06 月</div>
    <div class="xlab" style="left:700px">08 月</div>
    <div class="xlab" style="left:1030px">10 月</div>
    <div class="xlab" style="left:1330px">11-11</div>
    <div class="xlab" style="left:1500px">12 月</div>
  </div>
  <div class="note fx" id="e5">2025-05-18 禁酒令落地，6 月散瓶首破 2,000；8 月失守 1,800；10 月破 1,700；
    11-11 电商补贴把散瓶打到 <b>1,399</b>，首次跌破 1,499 指导价；12 月全面停货，价格才回到 1,600。</div>
</div>
""",
    "cues": [
        {"t": 200, "sel": "#e1", "act": "on"},
        {"t": 500, "sel": "#e2", "act": "on"},
        {"t": 1000, "sel": "#e3", "act": "on"},
        {"t": 1300, "sel": "#e4", "act": "on"},
        {"t": 4000, "sel": "#e5", "act": "on"},
    ],
}

S37 = {
    "id": "3-7",
    "title": "五粮液 2026：303 亿元被涂改掉",
    "dur": 20,
    "bg": "#f4f1e8",
    "ink": "#1d2a24",
    "accent": "#0f5132",
    "muted": "#7d8a80",
    "font": SANS,
    "sub": "3-7 · 纵向事件链 · 22,144",
    "css": """
.chain{position:absolute;inset:0;background:linear-gradient(180deg,#f7f4ec 0%,#f4f1e8 60%,#eeeade 100%)}
.kick{position:absolute;left:96px;top:80px;font:700 19px/1 Consolas,monospace;letter-spacing:.4em;color:#0f5132}
.h1{position:absolute;left:94px;top:116px;font:700 70px/1.18 "__FONT__"}
.h1 em{font-style:normal;color:#b91c1c}
.line{position:absolute;left:150px;top:300px;bottom:250px;width:3px;background:rgba(15,81,50,.25)}
.ev{position:absolute;left:150px;right:96px;padding-left:70px}
.ev .d{position:absolute;left:-9px;top:8px;width:21px;height:21px;border-radius:50%;
  background:#f4f1e8;border:3px solid #0f5132}
.ev .dt{font:700 17px/1 Consolas,monospace;color:#0f5132;letter-spacing:.08em;margin-bottom:8px}
.ev .tt{font:700 30px/1.35 "__FONT__";margin-bottom:6px}
.ev .tx{font:400 19px/1.6 "__FONT__";color:#4b5a52;max-width:1180px}
.ev.hot .d{border-color:#b91c1c;background:#b91c1c}
.ev.hot .dt{color:#b91c1c}
.ev.hot .tt{color:#b91c1c}
.foot{position:absolute;right:96px;bottom:56px;font:400 15px/1 Consolas,monospace;color:#8a968c;letter-spacing:.08em}
""",
    "body": """
<div class="chain">
  <div class="kick fx" id="f1">TIMELINE · 2025-02 → 2026-05</div>
  <div class="h1 fx d1" id="f2">一条链，<em>303 亿元</em>凭空消失</div>
  <div class="line"></div>
  <div class="ev fx" id="f3" style="top:298px">
    <div class="d"></div><div class="dt">2025-02-12</div>
    <div class="tt">两家「平台公司」同日成立</div>
    <div class="tx">四川五钧、四川五浚各 5 亿元级，39 家一级经销商持股，法人是刚离任的大区高管。</div></div>
  <div class="ev fx" id="f4" style="top:464px">
    <div class="d"></div><div class="dt">2025-08 中报</div>
    <div class="tt">前五大客户占比 21.12% → 56.96%</div>
    <div class="tx">同一批经销商被装进「平台」，收入提前确认，市场称其为业绩放大器。</div></div>
  <div class="ev hot fx" id="f5" style="top:630px">
    <div class="d"></div><div class="dt">2026-04-30 深夜</div>
    <div class="tt">《前期会计差错更正》：收入确认改为「终端售出」</div>
    <div class="tx">前三季度营收 609.45 → 306.38 亿元，一次性抹掉 303.08 亿元；新增「监管商品款」等科目 312.22 亿元。</div></div>
  <div class="ev hot fx" id="f6" style="top:796px">
    <div class="d"></div><div class="dt">2026-05-06</div>
    <div class="tt">复牌低开 6.49%，20 天跌到 85.47 元</div>
    <div class="tx">当晚抛出 30–50 亿元增持；投资者把这次调整称作「涂改液」，年报「会计政策变更」一栏却写着「不适用」。</div></div>
  <div class="foot">数据：公司公告、东方财富、证券之星（2026-05）</div>
</div>
""",
    "cues": [
        {"t": 200, "sel": "#f1", "act": "on"},
        {"t": 500, "sel": "#f2", "act": "on"},
        {"t": 1100, "sel": "#f3", "act": "on"},
        {"t": 2100, "sel": "#f4", "act": "on"},
        {"t": 3500, "sel": "#f5", "act": "on"},
        {"t": 5600, "sel": "#f6", "act": "on"},
    ],
}

S41 = {
    "id": "4-1",
    "title": "结论：谁的报表更能扛",
    "dur": 20,
    "bg": "#080c18",
    "ink": "#e8eefc",
    "accent": "#f5c451",
    "muted": "#6b7a99",
    "font": SANS,
    "sub": "4-1 · 双卡对照收束 · 23,616",
    "css": """
.fin{position:absolute;inset:0;background:
  radial-gradient(80% 70% at 50% -10%,#132146 0%,#0b1226 45%,#080c18 80%)}
.kick{position:absolute;left:96px;top:80px;font:700 19px/1 Consolas,monospace;letter-spacing:.42em;color:#f5c451}
.h1{position:absolute;left:94px;top:118px;font:700 74px/1.16 "__FONT__"}
.h1 em{font-style:normal;color:#f5c451}
.cards{position:absolute;left:96px;right:96px;top:320px;display:flex;gap:36px}
.card{flex:1;background:rgba(255,255,255,.045);border:1px solid rgba(255,255,255,.10);
  border-radius:10px;padding:44px 46px 38px;position:relative}
.card.top{border-color:rgba(245,196,81,.45);background:rgba(245,196,81,.055)}
.card h3{font:700 30px/1.2 "__FONT__";margin-bottom:8px}
.card .sc{font:400 14px/1 Consolas,monospace;letter-spacing:.2em;color:#8b9ab5;margin-bottom:26px}
.card ul{list-style:none}
.card li{font:400 20px/1.75 "__FONT__";color:#c6d2e8;padding-left:20px;position:relative;margin-bottom:12px}
.card li:before{content:"";position:absolute;left:0;top:13px;width:7px;height:7px;border-radius:50%;background:#f5c451}
.card li b{color:#fff;font-family:Consolas,monospace}
.card .rd{margin-top:22px;font:400 17px/1.7 "__FONT__";color:#93a3bf}
.verdict{position:absolute;left:96px;right:96px;bottom:120px;border-top:1px solid rgba(245,196,81,.28);
  padding-top:30px;display:flex;justify-content:space-between;align-items:flex-end;gap:50px}
.verdict .t{font:700 34px/1.4 "__FONT__";max-width:1180px}
.verdict .t b{color:#f5c451;font-family:Consolas,monospace}
.verdict .src{font:400 14px/1.9 Consolas,monospace;color:#6b7a99;text-align:right;white-space:nowrap}
""",
    "body": """
<div class="fin">
  <div class="kick fx" id="g1">CONCLUSION</div>
  <div class="h1 fx d1" id="g2">一家在<em>收</em>，一家在<em>扛</em></div>
  <div class="cards">
    <div class="card top fx d2" id="g3">
      <h3>贵州茅台</h3>
      <div class="sc">10 项比率领先 9 项</div>
      <ul>
        <li>毛利率 <b>91.18%</b>、净利率 <b>48.76%</b>、资本回报 <b>46.29%</b></li>
        <li>资产负债率仅 <b>19.64%</b>，流动比率 <b>5.09×</b></li>
        <li>唯一的「慢」是 1,419 天存货周转，属基酒陈酿工艺</li>
      </ul>
      <div class="rd">2025 首次营收净利双降，靠控量保价换来价格体系不塌。</div>
    </div>
    <div class="card fx d2" id="g4">
      <h3>五粮液</h3>
      <div class="sc">仅存货周转速度一项占优</div>
      <ul>
        <li>毛利率 <b>77.54%</b> 仍在，但营业利润率掉到 <b>30.23%</b></li>
        <li>资本回报 <b>9.46%</b>，已接近资金成本</li>
        <li>资产负债率 <b>55.49%</b>，其中 163.25 亿元是待确认预收款</li>
      </ul>
      <div class="rd">303 亿元收入一次性回退，修复路径只有一条：把收入拉回来。</div>
    </div>
  </div>
  <div class="verdict fx" id="g5">
    <div class="t">同样是高端白酒，<b>一个在收杠杆、一个在扛库存</b>。2026 年真正要盯的是两家的合同负债与批发价。</div>
    <div class="src">数据：2024 / 2025 年报（合并口径）<br>金额单位：万元</div>
  </div>
</div>
""",
    "cues": [
        {"t": 200, "sel": "#g1", "act": "on"},
        {"t": 500, "sel": "#g2", "act": "on"},
        {"t": 1100, "sel": "#g3", "act": "on"},
        {"t": 1400, "sel": "#g4", "act": "on"},
        {"t": 3400, "sel": "#g5", "act": "on"},
    ],
}

SHOTS = [S34, S35, S36, S37, S41]
