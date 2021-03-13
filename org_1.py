

import numpy
from medpy.filter.smoothing import anisotropic_diffusion

from skimage import color
from skimage import io
import math
from PIL import Image
for o in range(250):
    msk = Image.open('/Users/ashishkumar/Desktop/diffusion/t7m.png')
    img =Image.open('/Users/ashishkumar/Desktop/diffusion/t7.png')
    img2= Image.new(img.mode,img.size)
    pixNew =img2.load()
    
    
    mask = msk.load()
    image = img.load()
    msk2= Image.new(msk.mode,msk.size)
    
    mask2=msk2.load()
    
        
        
    for i in range(3,img.size[0]-2):
        for j in range(3,img.size[1]-2):
            if mask[i,j][0]==255:
                mask2[i-1,j]=(0,0,0,255)
                mask2[i+1,j]=(0,0,0,255)
                mask2[i,j-1]=(0,0,0,255)
                mask2[i,j+1]=(0,0,0,255)
                mask2[i,j]=(0,0,0,255)
                Ix=(image[i+1,j][0]-image[i-1,j][0])/2
                Iy=(image[i,j+1][0]-image[i,j-1][0])/2
                denN=math.sqrt((Ix*Ix)+(Iy*Iy)+0.000001)
                Nx=Ix/denN
                Ny=Iy/denN
                    
                p1=i+1
                q1=j
                Lnew1 =image[p1+1,q1][0]+image[p1-1,q1][0]+image[p1,q1+1][0]+image[p1,q1-1][0]-4*image[p1,q1][0]
                p2=i-1
                q2=j
                Lnew2 =image[p2+1,q2][0]+image[p2-1,q2][0]+image[p2,q2+1][0]+image[p2,q2-1][0]-4*image[p2,q2][0]
                p3=i
                q3=j+1
                Lnew3 =image[p3+1,q3][0]+image[p3-1,q3][0]+image[p3,q3+1][0]+image[p3,q3-1][0]-4*image[p3,q3][0]
                p4=i
                q4=j-1
                Lnew4 =image[p4+1,q4][0]+image[p4-1,q4][0]+image[p4,q4+1][0]+image[p4,q4-1][0]-4*image[p4,q4][0]
                deLx = Lnew1 - Lnew2
                deLy = Lnew3 - Lnew4
                    
                beta=0.05*((deLx*(-Ny))+(deLy*Nx))
                    
                Ixf=image[i+1,j][0]-image[i,j][0]
                Ixb=image[i,j][0]-image[i-1,j][0]
                Iyf=image[i,j+1][0]-image[i,j][0]
                Iyb=image[i,j][0]-image[i,j-1][0]
                Ixfm=min(Ixf,0)
                IxfM=max(Ixf,0)
                Ixbm=min(Ixb,0)
                IxbM=max(Ixb,0)
                Iyfm=min(Iyf,0)
                IyfM=max(Iyf,0)
                Iybm=min(Iyb,0)
                IybM=max(Iyb,0)
                    
                if beta>0:
                    ModeLI=math.sqrt((Ixbm*Ixbm)+(IxfM*IxfM)+(Iybm*Iybm)+(IyfM*IyfM))
                elif beta<=0:
                    ModeLI=math.sqrt((IxbM*IxbM)+(Ixfm*Ixfm)+(IybM*IybM)+(Iyfm*Iyfm))
                It=beta*ModeLI
                k=list(image[i,j])
                    
                g= k[0] +0.1*(It)
                    
                g=int(g)
                if g<0:
                    g=0
                if g>255:
                    g=255
                print(g)
                    
                pixNew[i,j] = (g,g,g,255)

            else:
                pixNew[i,j]=image[i,j]
    
    img2.save("t7m1.png")                   
    img.close()
    
    img2.show()           
    img2.close()



	if (o%20)=0:
	img=numpy.asarray(Image.open('/Users/ashishkumar/Desktop/diffusion/t7m1.png'))

	img_filtered = anisotropic_diffusion(img)
	img2=Image.fromarray(numpy.uint8(img_filtered))
	img2.save("t7m1.png")
	img2.show()
        

                
                