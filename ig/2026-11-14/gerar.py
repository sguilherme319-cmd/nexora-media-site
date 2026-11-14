import sys,os; sys.path.insert(0,'/home/claude/nexora-media-site/ig/_gerador')
from lib import *
C='/home/claude/cat/hi-%02d.png'; O=os.path.dirname(os.path.abspath(__file__))+'/'
# IMPERIAL
imperial_post(C%56,(390,430,800,1215),'Lattafa','Yara',['Tangerina','Orquídea','Baunilha','Almíscar'],'Doce, delicado e envolvente. O queridinho das mulheres.',O+'imp_10h_yara.jpg')
imperial_story(C%49,(395,400,790,1210),'Caixinha da Imperial','O que te impede de comprar um perfume importado hoje?',O+'imp_13h_story.jpg')
imperial_cover(['Os 5 árabes','masculinos'],'que mais fazem sucesso na Imperial',[(C%5,(560,520,900,900)),(C%9,(430,380,800,1000)),(C%10,(400,445,800,1110))],O+'imp_16h_c1.jpg')
prods=[(5,(350,410,921,896),'Lattafa','Khamrah',['Tâmaras','Canela','Baunilha'],'Doce e quente. O mais pedido do inverno.'),
 (9,(415,362,921,995),'Lattafa','Asad',['Pimenta preta','Tabaco','Baunilha'],'Intenso e poderoso. Presença garantida.'),
 (8,(390,380,880,1130),'Armaf','Club de Nuit',['Abacaxi','Bétula','Baunilha'],'Elegante e marcante. Um clássico árabe.'),
 (49,(395,400,790,1210),'Rasasi','Hawas',['Bergamota','Canela','Âmbar'],'Fresco e aquático. Perfeito para o dia a dia.'),
 (10,(400,445,800,1110),'Lattafa','Fakhar Black',['Maçã','Gengibre','Lavanda'],'Moderno e versátil. Do dia à noite.')]
for i,(p,cr,b,n,no,t) in enumerate(prods,2):
    imperial_post(C%p,cr,b,n,no,t,O+f'imp_16h_c{i}.jpg',badge=f'{i-1}/5')
imperial_cta('Qual é o seu?',['Comenta o número do seu favorito','ou chama a gente no direct para','consultar a disponibilidade.'],O+'imp_16h_c7.jpg')
imperial_post(C%4,(410,345,860,1150),'Afnan','9 PM',['Maçã','Canela','Baunilha'],'Intenso e sedutor. Feito para a noite.',O+'imp_20h_9pm.jpg')
# NEXORA
nexora_post('Seu concorrente posta todo dia no Instagram.','E a sua empresa?',['Artes e vídeos com a cara da sua marca','Postagens organizadas toda semana','Anúncios para quem é da sua região'],'QUERO UM ORÇAMENTO: (49) 99808-8624',O+'nex_10h.jpg',kicker='Gestão de Instagram')
nexora_story('Pergunta rápida','Qual é o maior desafio do seu negócio no Instagram hoje?','Falta de tempo, de ideias, de seguidores ou de vendas? Me conta que eu te ajudo.',O+'nex_13h_story.jpg')
nexora_post('3 sinais de que a sua empresa','precisa de um site',['Leva 30 segundos para ler','Salve para revisar o seu negócio depois'],'ARRASTE PARA VER  >>',O+'nex_16h_c1.jpg',kicker='Carrossel')
sl=[('Cliente pergunta preço e horário toda hora','Um site responde tudo isso 24 horas por dia, sem você parar o que está fazendo.'),
    ('Você só existe no Instagram','Se a conta cair ou o alcance despencar, seus clientes não têm outro lugar para te encontrar.'),
    ('Seu concorrente aparece no Google e você não','Quem procura o seu serviço na cidade acaba chegando primeiro em quem tem site.')]
for i,(t,b) in enumerate(sl,1): nexora_slide(i,t,b,O+f'nex_16h_c{i+1}.jpg',total=3)
nexora_post('Site profissional e rápido','e com pedido no seu WhatsApp.',['Feito para o seu tipo de negócio','Você só manda as informações'],'QUERO MEU SITE: (49) 99808-8624',O+'nex_16h_c5.jpg',kicker='Nexora Media')
nexora_post('Você manda as fotos.','A gente entrega o vídeo.',['Vídeo da sua loja, produto ou ambiente','Feito só com as suas imagens','Pronto para postar e anunciar'],'QUERO MEU VÍDEO: (49) 99808-8624',O+'nex_20h.jpg',kicker='Vídeos para empresas')
print('ok')
