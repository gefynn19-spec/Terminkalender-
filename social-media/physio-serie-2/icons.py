# -*- coding: utf-8 -*-
"""Icons und Illustrationen der zweiten Staffel.

Die Strich-Icons der ersten Serie werden mitbenutzt, ergaenzt um vier neue.
"""
import importlib.util
import os

_pfad = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'physio-serie', 'icons.py')
_spec = importlib.util.spec_from_file_location('icons_serie1', _pfad)
_serie1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_serie1)
BASIS = _serie1.ICONS

EXTRA = {
    'greifen': '<path d="M18 26v14"></path><path d="M26 20v20"></path><path d="M34 22v18"></path>'
               '<path d="M42 28v12"></path>'
               '<path d="M14 38c0 12 8 20 18 20h6c8 0 14-6 14-14V30"></path>'
               '<path d="M14 38h-4a4 4 0 0 0 0 8h4"></path>',
    'stufen': '<path d="M6 42h12V30h12V18h12V6h4"></path><path d="M6 42v-6"></path>'
              '<path d="M6 42h40"></path>',
    'kribbeln': '<path d="M16 40V24"></path><path d="M24 40V16"></path><path d="M32 40V20"></path>'
                '<path d="M12 44h26"></path>'
                '<path d="M40 12l6-4M42 22h7M40 32l6 4"></path>',
    'haltung': '<path d="M12 6v36" stroke-dasharray="4 5" opacity="0.5"></path>'
               '<circle cx="27" cy="10" r="6"></circle><path d="M24 16C16 22 15 32 20 43"></path>'
               '<path d="M22 27l10 4"></path>',
}

ICONS = dict(BASIS, **EXTRA)


def _markierung(cx, cy, r):
    return ('<circle cx="%d" cy="%d" r="%d" fill="#8C1010" opacity="0.16" stroke="none"></circle>'
            % (cx, cy, r))


HEROES = {
    # Stehende Figur, Hueftgelenk markiert
    'huefte': _markierung(55, 58, 16) +
              '<circle cx="55" cy="16" r="11"></circle><path d="M55 27v31"></path>'
              '<path d="M55 34l-17 13M55 34l15 15"></path>'
              '<path d="M53 58l-7 26v24M57 58l9 25 2 25"></path>'
              '<path d="M10 112h100"></path>',
    # Kopf im Profil, Kiefergelenk markiert
    'kiefer': '<circle cx="38" cy="62" r="15" fill="#8C1010" opacity="0.16" stroke="none"></circle><path d="M30 32C30 17 44 8 58 10c16 2 26 14 26 28 0 8-3 14-7 19l6 9c2 3 0 6-3 6h-6v8c0 6-5 10-11 10H48c-10 0-18-9-18-20z"></path><path d="M38 62c4 13 14 22 25 24"></path><path d="M48 90v12M74 88v14"></path><path d="M22 114c8-11 20-16 32-16s24 5 32 16"></path>',
    'ellenbogen': _markierung(64, 58, 16) +
                  '<circle cx="28" cy="22" r="10"></circle>'
                  '<path d="M34 30l30 28"></path><path d="M64 58l-18 38"></path>'
                  '<circle cx="43" cy="103" r="8"></circle>',
    # Hand mit markiertem Handgelenk
    'hand': '<circle cx="63" cy="98" r="14" fill="#8C1010" opacity="0.16" stroke="none"></circle><rect x="44" y="52" width="38" height="38" rx="12"></rect><path d="M52 52V34M62 52V28M72 52V31M80 52V40"></path><path d="M44 66l-14 7"></path><path d="M52 90v14M74 90v14"></path>',
    'ferse': '<circle cx="42" cy="90" r="16" fill="#8C1010" opacity="0.16" stroke="none"></circle><path d="M54 12v46c0 14-12 18-12 32h48" stroke-width="11"></path><path d="M12 106h96"></path>',
    'reha': '<circle cx="44" cy="16" r="11"></circle><path d="M44 27v27"></path>'
            '<path d="M44 35l24 12"></path><path d="M72 47v55"></path><path d="M64 102h16"></path>'
            '<path d="M42 54l-8 26v22M46 54l8 25 2 23"></path>'
            '<path d="M10 112h100"></path>',
    # Bein mit Abflussrichtung
    'lymphe': '<path d="M42 8c-7 24-7 44-3 60 3 12 3 22 1 32"></path><path d="M78 8c5 24 3 44-2 60-3 12-3 22-1 32"></path><path d="M40 100h36c11 0 19 4 19 8H40z"></path><path d="M50 86l10-10 10 10M50 64l10-10 10 10M50 42l10-10 10 10"></path>',
    'schwangerschaft': '<circle cx="42" cy="16" r="11"></circle>'
                       '<path d="M42 27c-5 13-5 27-1 40"></path>'
                       '<path d="M45 38c15 2 24 13 24 24s-9 19-24 21"></path>'
                       '<path d="M42 42l-13 17"></path>'
                       '<path d="M41 84l-7 16v12M45 84l8 16 2 12"></path>'
                       '<path d="M10 112h100"></path>',
    # Einbeinstand am Handlauf
    'sturzprophylaxe': '<circle cx="42" cy="16" r="11"></circle><path d="M42 27v27"></path>'
                       '<path d="M42 35l30 8"></path>'
                       '<path d="M44 54l2 26v24"></path><path d="M42 54l-15 17 9 13"></path>'
                       '<path d="M88 26v78"></path><path d="M88 44h12M88 86h12"></path>'
                       '<path d="M10 112h100"></path>',
    # Langer Roehrenknochen
    'knochen': '<path d="M42 36l38 50" stroke-width="15"></path>'
               '<circle cx="34" cy="28" r="12"></circle><circle cx="48" cy="20" r="11"></circle>'
               '<circle cx="88" cy="94" r="12"></circle><circle cx="74" cy="102" r="11"></circle>',
}
