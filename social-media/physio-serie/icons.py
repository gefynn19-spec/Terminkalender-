# -*- coding: utf-8 -*-
"""Strich-Icons (viewBox 0 0 48 48) und Themen-Illustrationen (viewBox 0 0 160 120)."""

ICONS = {
    'sitzen': '<circle cx="16" cy="11" r="6"></circle><path d="M16 17c-5 4-6 10-5 15"></path>'
              '<path d="M13 23l13 8"></path><path d="M11 32h11v11"></path>'
              '<path d="M26 31h17"></path><path d="M39 31v12"></path>',
    'druck': '<path d="M24 5v22"></path><path d="M14 19l10 10 10-10"></path><path d="M7 40h34"></path>',
    'gewicht': '<path d="M7 18v12M14 13v22M34 13v22M41 18v12"></path><path d="M14 24h20"></path>',
    'stress': '<circle cx="27" cy="18" r="10"></circle><path d="M27 28v6"></path>'
              '<path d="M16 42c2-5 6-7 11-7s9 2 11 7"></path><path d="M7 6l5 5M3 20h7M7 33l5-5"></path>',
    'unsicher': '<circle cx="24" cy="7" r="5"></circle><path d="M24 12v13"></path><path d="M13 17h22"></path>'
                '<path d="M24 25l-6 10M24 25l6 10"></path><path d="M5 41q4.75-6 9.5 0t9.5 0t9.5 0t9.5 0"></path>',
    'fuss': '<path d="M15 8c0 10 2 15 2 21 0 4 3 7 8 7h11c4 0 6-2 6-5 0-6-8-9-11-14"></path>'
            '<path d="M7 43h34"></path>',
    'zeit': '<circle cx="24" cy="24" r="18"></circle><path d="M24 13v11l8 5"></path>',
    'blitz': '<path d="M27 4L13 27h9l-3 17 15-24h-9l2-16z"></path>',
    'nacht': '<path d="M39 29A16 16 0 1 1 21 9a13 13 0 0 0 18 20z"></path>',
    'gelenk': '<path d="M24 4v10"></path><circle cx="24" cy="22" r="8"></circle>'
              '<path d="M24 30v10"></path><path d="M16 44h16"></path>',
    'wiederholung': '<path d="M41 24a17 17 0 1 1-5-12"></path><path d="M41 5v10H31"></path>',
    'tropfen': '<path d="M24 5s12 14 12 21a12 12 0 0 1-24 0c0-7 12-21 12-21z"></path>',
    'waage': '<path d="M24 6v34M14 41h20"></path><path d="M7 15h34"></path>'
             '<path d="M7 15L2 28a6 6 0 0 0 10 0z"></path><path d="M41 15l-5 13a6 6 0 0 0 10 0z"></path>',
    'frage': '<circle cx="24" cy="24" r="18"></circle><path d="M19 19a5 5 0 1 1 5 6v3"></path>'
             '<path d="M24 34v1"></path>',
}

def _wirbel(cx, cy, angle, w=40):
    return ('<rect x="%d" y="%d" width="%d" height="13" rx="6.5" transform="rotate(%d %d %d)"></rect>'
            % (cx - w // 2, cy - 6, w, angle, cx, cy))

# Illustrationen, viewBox 0 0 120 120 - jede fuellt die Flaeche
HEROES = {
    # Lendenwirbelsaeule mit Becken und Beweglichkeitsbogen
    'ruecken': '<rect x="34" y="12" width="44" height="12" rx="6"></rect><path d="M34 18h-14"></path><rect x="34" y="30" width="44" height="12" rx="6"></rect><path d="M34 36h-14"></path><rect x="34" y="48" width="44" height="12" rx="6"></rect><path d="M34 54h-14"></path><rect x="34" y="66" width="44" height="12" rx="6"></rect><path d="M34 72h-14"></path>'
               '<path d="M36 84h40l-6 20a10 10 0 0 1-28 0z"></path>'
               '<path d="M96 26a36 36 0 0 1 0 68"></path>'
               '<path d="M88 34l8-10 10 8"></path>',
    'knie': '<circle cx="80" cy="72" r="17" fill="#8C1010" opacity="0.16" stroke="none"></circle><circle cx="60" cy="16" r="11"></circle><path d="M58 27v23"></path><path d="M58 33l17 9M58 33l-17 9"></path><path d="M58 50l22 22v34"></path><path d="M80 106h15"></path><path d="M58 50l-20 24-13 26"></path><path d="M25 100l-11 6"></path><path d="M10 112h100"></path>',
    'schulter': '<circle cx="50" cy="40" r="14" fill="#8C1010" opacity="0.16" stroke="none"></circle><circle cx="50" cy="14" r="10"></circle><path d="M50 24v39"></path><path d="M50 36l25-9 16-15"></path><path d="M50 41l-18 16"></path><path d="M50 63l-11 26-2 21M50 63l12 26 4 21"></path><path d="M10 112h100"></path>',
    'sprunggelenk': '<circle cx="60" cy="98" r="15" fill="#8C1010" opacity="0.16" stroke="none"></circle><circle cx="56" cy="16" r="11"></circle><path d="M56 27v24"></path><path d="M56 34l-21 8M56 34l21 8"></path><path d="M56 51l4 25v22"></path><path d="M60 98h17"></path><path d="M56 51l-17 20 11 15"></path><path d="M10 108h100"></path>',
    'buero': '<circle cx="33" cy="24" r="12"></circle><path d="M33 36c-8 8-11 20-9 31"></path>'
             '<path d="M28 56l27 13"></path><path d="M16 67h26v37"></path>'
             '<path d="M16 67V38"></path><path d="M56 80h54"></path>'
             '<path d="M63 80v30M103 80v30"></path>'
             '<rect x="70" y="38" width="38" height="28" rx="4"></rect><path d="M89 66v14"></path>'
             '<path d="M10 112h100"></path>',
    # Becken mit Beckenboden-Schlinge
    'beckenboden': '<path d="M22 34c0 40 16 62 38 62s38-22 38-62"></path>'
                   '<path d="M22 34c-10-20 6-32 20-25M98 34c10-20-6-32-20-25"></path>'
                   '<path d="M32 62c12 26 44 26 56 0" stroke-dasharray="7 8"></path>'
                   '<path d="M60 88V58"></path><path d="M50 68l10-10 10 10"></path>',
    # Laufende Figur
    'sport': '<circle cx="74" cy="20" r="11"></circle>'
             '<path d="M70 32L58 64"></path>'
             '<path d="M67 42l28-9M63 52l-27 9"></path>'
             '<path d="M58 64l22 17-6 27"></path>'
             '<path d="M58 64l-17 21-20 11"></path>'
             '<path d="M10 112h100"></path>',
}
