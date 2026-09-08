import numpy as np
import matplotlib.pyplot as plt 

im = np.empty(shape = (91,91,3), dtype = np.uint8)

im[:,:] = (0,255,0)

#print(im[0,0])
#print(im[90,90])

for i in range(9) :
    im[i*10,:] = (0,0,255)
    im[:,i*10] = (0,0,255)

#plt.imshow(im)

im_les_mines = plt.imread("data/les-mines.jpg")
#print(im_les_mines.flags.writeable)
im_les_mines = np.copy(im_les_mines)
#print(im_les_mines_copy.flags.writeable)

#plt.imshow(im_les_mines_copy)

print(type(im_les_mines))
print(im_les_mines.shape)
print(im_les_mines.itemsize)
print(im_les_mines.dtype)
print(im_les_mines.max(), im_les_mines.min())


#plt.imshow(im_les_mines_copy[:10,:10])


# ---partie accès partie---


#plt.imshow(im_les_mines_copy[::20,::20])

def isoler (image, l,c) :
    debut_ligne = image.shape[0]//2 - l//2
    fin_ligne = debut_ligne + l
    debut_colonne = image.shape[1]//2 - c//2
    fin_colonne = debut_colonne + c
    return image[debut_ligne:fin_ligne,debut_colonne:fin_colonne]

#plt.imshow(isoler(im_les_mines_copy, 100, 200))


# ---partie canaux---


im_r = im_les_mines[:,:,0]
im_g = im_les_mines[:,:,1]
im_b = im_les_mines[:,:,2]

#plt.imshow(im_r, cmap='Reds');plt.show()
#plt.imshow(im_g, cmap='Greens');plt.show()
#plt.imshow(im_b, cmap='Blues');plt.show()

im_copy = np.copy(im_les_mines)

im_copy[-200:-1,-200:-1] = (219, 112, 147)

#plt.imshow(im_copy)

im_copy[-200:-1,-200:-1] = (255, 255, 255)
im_copy[-200:-1:2,-200:-1] = (255, 0, 0)

#plt.imshow(im_copy);plt.show()
#plt.imshow(im_copy[-20:-1,-20:-1]);plt.show()


# ---partie transparence---


(l,c,_) = im_les_mines.shape
im_transparence = np.empty(shape = (l,c,4), dtype = np.uint8)
im_transparence[:,:,:3] = im_les_mines
im_transparence[:,:,3] = 128

#plt.imshow(im_transparence)


# ---partie gris---


im_gris = np.copy(im_les_mines)
im_gris[:,:,:] = im_gris[:,:,:]/255

#plt.imshow(im_gris)

im_gris_a = np.copy(im_les_mines)
moy = (im_gris_a[:,:,0] + im_gris_a[:,:,1] + im_gris_a[:,:,2])/3
for i in range(3) :
    im_gris_a[:,:,i] = moy

#plt.imshow(im_gris_a);plt.show()

im_gris_b = np.copy(im_les_mines)
G = 0.299*im_gris_b[:,:,0] + 0.587*im_gris_b[:,:,1] + 0.114*im_gris_b[:,:,2]
for i in range(3) :
    im_gris_b[:,:,i] = G

#plt.imshow(im_gris_b);plt.show()

#im_gris_a[:,:,:] = im_gris_a[:,:,:]*im_gris_a[:,:,:]
im_gris_r = np.sqrt(im_gris_a)

#plt.imshow(im_gris_a);plt.show()


# ---partie affichage---


fig, axes = plt.subplots(3,3)
for i in range(3) :
    axes[i,i].imshow(im_gris_a)
    axes[i,(i+1)%3].imshow(im_gris_b)
    axes[i,(i+2)%3].imshow(im_gris_r)
plt.show()