import collections
import re

from bs4 import BeautifulSoup

TEST_URL = 'http://test-web-wordpress.epfl.ch'
SECTIONS_TO_REMOVE = ['recent-comments-2', 'archives-2', 'categories-2', 'meta-2', 'search-2']
CSS_TO_MODIFY = ['style.css', 'stylisticss.grid.css']

class Filter:
    def response(self, flow):
        url = flow.request.url
        # Modifier le html pour filtrer les bugs
        if url[len(url) - 1] == '/' or url[len(url)-5:] == '.html' or url[len(url)-4:] == '.jsp':
            html = BeautifulSoup(flow.response.content, 'html.parser')
            # Modifications apportées aux nouvelles versions du site
            if url[:len(TEST_URL)] == TEST_URL:
                # Enlever la barre additionelle inutile des réseaux sociaux
                for div in html.findAll('div', {'class' : 'addtoany_share_save_container addtoany_content_top'}):
                    div.extract()
                
                # Retrier les elements dans la barre de droite
                aside = html.find('aside' , {'id' : 'secondary'})
                toSort = {}
                for section in aside.findAll('section'):
                    sectionId = section['id']
                    if sectionId[:len(sectionId) - 2] == 'black-studio-tinymce':
                        toSort[sectionId] = section.extract()
                sortedSections = list(map(lambda x : x[1], sorted(toSort.items())))
                for section in sortedSections:
                    aside.append(section)

                # Enlever la barre de droite de Wordpress
                for section in html.findAll('section'):
                    if section.get('id') in SECTIONS_TO_REMOVE:
                        section.extract()

                # Supprimer le footer du site
                for footer in html.findAll('footer', {'id' : 'colophon'}):
                    footer.extract()
                        
            # Modifications apportées aux sites originaux
            else:
                # Supprimer le footer du site
                for div in html.findAll('div', {'id' : 'footer'}):
                    div.extract()

            # Mettre les changements dans la réponse
            flow.response.content = str(html).encode('utf-8')

        # Modifier le .css pour enlever le mode résponsif
        parts = url.split('/')
        fileName = parts[len(parts) - 1].strip('/')
        if '.css' in fileName:
            css_mod = re.sub('@media screen and \(min-width: [0-9]*', '@media screen and (min-width: 1', flow.response.text)
            # Modifier les couleurs en rouge (sans prendre les nuances de gris)
            it = re.finditer('\#[a-f 0-9]{6}', css_mod)
            for color in it:
                pos = color.start()
                # Si ce n'est pas une nuance de gris
                if not ((css_mod[pos+1:pos+2] == css_mod[pos+3:pos+4]) and (css_mod[pos+3:pos+4] == css_mod[pos+5:pos+6])):
                    css_mod = css_mod[:pos] + "#ae0010" + css_mod[pos + 7:]

            flow.response.text = css_mod


def start():
    return Filter()

if __name__ == '__main__':
    print("C'est ici qu'on peut mettre des tests unitaires!")
