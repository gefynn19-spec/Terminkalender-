# -*- coding: utf-8 -*-
"""Erzeugt aus posts.py die 28 Artboards und die canvas.json der Serie."""
import json
from icons import ICONS, HEROES
from posts import POSTS

ROOT = ("width: 1080px; height: 1080px; box-sizing: border-box; background: #EFE7DA; color: #332A20; "
        "padding: 72px; display: flex; flex-direction: column; justify-content: space-between; "
        "overflow: hidden; font-family: 'Barlow', 'Helvetica Neue', Arial, sans-serif;")
ANTON = "'Anton', 'Impact', 'Haettenschweiler', sans-serif"
KARTE = "background: #FFFFFF; box-shadow: 0 12px 28px rgba(72, 48, 22, 0.10);"
PFEIL = ('<svg width="26" height="26" viewBox="0 0 48 48" fill="none" stroke="currentColor" '
         'stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round">'
         '<path d="M7 24h32"></path><path d="M27 12l12 12-12 12"></path></svg>')
HAKEN = ('<svg width="52" height="52" viewBox="0 0 48 48" fill="none" style="flex-shrink: 0;">'
         '<circle cx="24" cy="24" r="22" fill="#8C1010"></circle>'
         '<path d="M14 25l7 7 14-16" stroke="#F7F2E8" stroke-width="4.2" fill="none" '
         'stroke-linecap="round" stroke-linejoin="round"></path></svg>')

BRAND = ('  <div style="display: flex; align-items: center; gap: 16px;">\n'
         '    <div style="width: 18px; height: 18px; background: #8C1010;"></div>\n'
         '    <div style="font-size: 21px; font-weight: 600; letter-spacing: 0.22em; '
         'text-transform: uppercase; color: #8A7A66;">Gerstner Physiotherapie</div>\n  </div>')


def fuss(nr, letzte=False):
    links = ('' if letzte else
             '<div style="display: flex; align-items: center; gap: 12px;">'
             '<span>Weiterwischen</span>%s</div>' % PFEIL)
    justify = 'flex-end' if letzte else 'space-between'
    return ('  <div style="display: flex; align-items: center; justify-content: %s; font-size: 20px; '
            'font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase; color: #A2937E;">'
            '%s<div>0%d / 04</div></div>' % (justify, links, nr))


def seite(inhalt, nr, letzte=False):
    return ('<!doctype html>\n<html>\n<head>\n  <meta charset="utf-8">\n'
            '  <script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
            '  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
            'family=Anton&family=Barlow:wght@400;500;600;700&display=swap">\n  <style>\n'
            "    body { margin: 0; font-family: 'Barlow', 'Helvetica Neue', Arial, sans-serif; }\n"
            '    a { color: #8C1010; } a:hover { color: #6B0C0C; }\n  </style>\n</helmet>\n'
            '<div style="%s">\n\n%s\n\n%s\n\n%s\n\n</div>\n</x-dc>\n'
            '<script data-dc-script data-props=\'{"$preview":{"width":1080,"height":1080}}\'>\n'
            'class Component extends DCLogic {\n  renderVals() {\n    return {};\n  }\n}\n'
            '</script>\n</body>\n</html>\n' % (ROOT, BRAND, inhalt, fuss(nr, letzte)))


def hook(p):
    if p.get('herobild'):
        hero = ('<img src="%s" alt="Anatomische Darstellung" '
                'style="width: 400px; height: 400px; display: block;">' % p['herobild'])
    else:
        hero = ('<svg width="350" height="350" viewBox="0 0 120 120" fill="none" stroke="#8C1010" '
                'stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round">%s</svg>'
                % HEROES[p['hero']])
    return (
        '  <div style="display: flex; flex-direction: column; align-items: flex-start; gap: 26px;">\n'
        '    <div style="font-family: %s; font-size: 100px; line-height: 0.94; letter-spacing: -0.005em; '
        'color: #8C1010; text-transform: uppercase; text-wrap: pretty;">Wusstest du schon?</div>\n'
        '    <div style="display: inline-flex; align-items: center; background: #8C1010; color: #F7F2E8; '
        'padding: 12px 28px 16px; transform: rotate(-1.5deg); font-family: %s; font-size: 62px; '
        'line-height: 1; letter-spacing: 0.02em; text-transform: uppercase;">%s</div>\n  </div>\n\n'
        '  <div style="display: flex; justify-content: center;">\n'
        '    <div style="background: #FFFFFF; padding: 18px 18px 54px; '
        'box-shadow: 0 22px 48px rgba(72, 48, 22, 0.20); transform: rotate(-2.5deg);">\n'
        '      <div style="width: 400px; height: 400px; background: #F7EDE8; display: flex; '
        'align-items: center; justify-content: center;">%s</div>\n    </div>\n  </div>'
        % (ANTON, ANTON, p['badge'], hero))


def anzeichen(p):
    karten = []
    for name, label in p['karten']:
        karten.append(
            '    <div style="%s padding: 32px 26px; display: flex; flex-direction: column; '
            'align-items: center; gap: 20px;">\n'
            '      <div style="width: 100px; height: 100px; border-radius: 50%%; background: #F7EDE8; '
            'display: flex; align-items: center; justify-content: center;">'
            '<svg width="54" height="54" viewBox="0 0 48 48" fill="none" stroke="#8C1010" '
            'stroke-width="3" stroke-linecap="round" stroke-linejoin="round">%s</svg></div>\n'
            '      <div style="font-size: 36px; font-weight: 700; line-height: 1.15; color: #332A20; '
            'text-align: center;">%s</div>\n    </div>' % (KARTE, ICONS[name], label))
    return (
        '  <div style="display: flex; flex-direction: column; gap: 20px;">\n'
        '    <div style="font-family: %s; font-size: 44px; line-height: 1; letter-spacing: 0.01em; '
        'text-transform: uppercase; color: #8C1010;">Wusstest du schon?</div>\n'
        '    <div style="font-size: 44px; font-weight: 600; line-height: 1.26; letter-spacing: -0.005em; '
        'color: #332A20; text-wrap: pretty; max-width: 900px;">%s</div>\n  </div>\n\n'
        '  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 26px;">\n'
        '%s\n  </div>' % (ANTON, p['aussage'], '\n\n'.join(karten)))


def behandlung(p):
    zeilen = []
    for punkt in p['punkte']:
        zeilen.append(
            '    <div style="display: flex; align-items: center; gap: 26px; %s padding: 22px 32px;">\n'
            '      %s\n'
            '      <div style="font-family: %s; font-size: 48px; line-height: 1.05; '
            'letter-spacing: 0.01em; color: #332A20;">%s</div>\n    </div>' % (KARTE, HAKEN, ANTON, punkt))
    return (
        '  <div style="display: flex; flex-direction: column; gap: 18px;">\n'
        '    <div style="display: flex; align-items: center; gap: 16px; color: #8C1010;">\n'
        '      <svg width="40" height="40" viewBox="0 0 48 48" fill="none" stroke="currentColor" '
        'stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M6 24h32"></path><path d="M26 12l12 12-12 12"></path></svg>\n'
        '      <div style="font-family: %s; font-size: 42px; line-height: 1; letter-spacing: 0.01em; '
        'text-transform: uppercase;">Daran arbeiten wir</div>\n    </div>\n'
        '    <div style="font-size: 40px; font-weight: 500; line-height: 1.28; color: #6A5B49; '
        'text-wrap: pretty; max-width: 860px;">%s</div>\n  </div>\n\n'
        '  <div style="display: flex; flex-direction: column; gap: 20px;">\n%s\n  </div>\n\n'
        '  <div style="background: #8C1010; color: #F7F2E8; padding: 34px 38px; font-size: 36px; '
        'font-weight: 600; line-height: 1.32; text-wrap: pretty;">%s</div>'
        % (ANTON, p['unter'], '\n\n'.join(zeilen), p['band']))


def termin(p):
    chat = ('<svg width="56" height="56" viewBox="0 0 48 48" fill="none" stroke="#8C1010" '
            'stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0;">'
            '<path d="M42 30a5 5 0 0 1-5 5H17L7 43V13a5 5 0 0 1 5-5h25a5 5 0 0 1 5 5z"></path>'
            '<path d="M17 20h14M17 27h9"></path></svg>')
    kalender = ('<svg width="56" height="56" viewBox="0 0 48 48" fill="none" stroke="#8C1010" '
                'stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0;">'
                '<rect x="6" y="11" width="36" height="31" rx="4"></rect>'
                '<path d="M6 21h36M16 6v9M32 6v9"></path><path d="M18 31l4 4 9-9"></path></svg>')
    pin = ('<svg width="52" height="52" viewBox="0 0 48 48" fill="none" stroke="currentColor" '
           'stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0;">'
           '<path d="M24 44s14-14.5 14-24a14 14 0 1 0-28 0c0 9.5 14 24 14 24z"></path>'
           '<circle cx="24" cy="20" r="5.5"></circle></svg>')

    def aktion(icon, text):
        return ('    <div style="display: flex; align-items: center; gap: 28px; %s padding: 30px 34px;">\n'
                '      %s\n      <div style="font-size: 38px; font-weight: 600; line-height: 1.22; '
                'color: #332A20;">%s</div>\n    </div>' % (KARTE, icon, text))

    return (
        '  <div style="font-family: %s; font-size: 72px; line-height: 1.06; letter-spacing: 0.005em; '
        'color: #8C1010; text-wrap: pretty;">%s</div>\n\n'
        '  <div style="display: flex; flex-direction: column; gap: 24px;">\n%s\n\n%s\n  </div>\n\n'
        '  <div style="background: #8C1010; color: #F7F2E8; padding: 34px 38px; display: flex; '
        'align-items: center; gap: 24px;">\n    %s\n'
        '    <div style="display: flex; flex-direction: column; gap: 6px;">\n'
        '      <div style="font-family: %s; font-size: 50px; line-height: 1.05; letter-spacing: 0.01em; '
        'text-transform: uppercase;">Gerstner Physiotherapie</div>\n'
        '      <div style="font-size: 26px; font-weight: 500; letter-spacing: 0.04em; color: #EBC9C9;">'
        'Zeiler Str. 20 · Sand am Main · 09524 5297</div>\n    </div>\n  </div>'
        % (ANTON, p['frage'], aktion(chat, 'Schreib es uns in die Kommentare'),
           aktion(kalender, 'Oder vereinbare einen Termin – wir helfen dir gerne weiter.'),
           pin, ANTON))


def bildtext(p):
    roh = lambda s: s.replace('<span style="color: #8C1010;">', '').replace('</span>', '').replace('&amp;', '&')
    return ('Bildunterschrift zum Kopieren:\n\nWusstest du schon?\n\n%s\n\n%s\n\n➡️ Daran arbeiten wir %s\n\n%s\n\n%s'
            '\n\n💬 %s Schreib es uns in die Kommentare oder vereinbare einen Termin – wir helfen dir gerne weiter.'
            '\n\n📍 Gerstner Physiotherapie · Zeiler Str. 20 · Sand am Main · 09524 5297'
            % (roh(p['aussage']), ', '.join(roh(k[1]) for k in p['karten']) + '.',
               p['unter'], '\n'.join('✔️ ' + roh(x) for x in p['punkte']), p['band'], p['frage']))


artboards, annotations, pages = [], [], []
for i, p in enumerate(POSTS, start=1):
    pid = 'page-%d' % i
    pages.append({'id': pid, 'name': '%d · %s' % (i, p['page'])})
    teile = [('Main' if i == 1 else p['key'] + 'Hook', hook(p), '1 · Hook', False),
             (p['key'] + 'Anzeichen', anzeichen(p), '2 · Anzeichen', False),
             (p['key'] + 'Behandlung', behandlung(p), '3 · Behandlung', False),
             (p['key'] + 'Termin', termin(p), '4 · Termin', True)]
    for nr, (stamm, inhalt, titel, letzte) in enumerate(teile, start=1):
        datei = stamm + '.dc.html'
        open(datei, 'w', encoding='utf-8').write(seite(inhalt, nr, letzte))
        artboards.append({'file': datei, 'title': titel, 'x': (nr - 1) * 1200, 'y': 0,
                          'w': 1080, 'h': 1080, 'print': 'fixed', 'page': pid})
    annotations.append({'id': 'caption-%d' % i, 'x': 0, 'y': 1180, 'w': 760,
                        'text': bildtext(p), 'page': pid})

canvas = {'artboards': artboards, 'annotations': annotations, 'pages': pages,
          'launch': {'view': 'canvas', 'page': 'page-1'}}
json.dump(canvas, open('canvas.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('%d Artboards, %d Seiten, %d Notizen geschrieben' % (len(artboards), len(pages), len(annotations)))
