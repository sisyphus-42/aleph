# aleph


Original :


![unnamed (1)](https://user-images.githubusercontent.com/58873465/194727703-01919212-873b-4bfd-96ad-c8d4e4a74cc2.jpg)



Inpainting in action:




![unnamed](https://user-images.githubusercontent.com/58873465/194727681-d41be46e-1ce3-4afa-b7d2-5faf68930526.gif)





![unnamed](https://user-images.githubusercontent.com/58873465/194727681-d41be46e-1ce3-4afa-b7d2-5faf68930526.gif)

![image](https://user-images.githubusercontent.com/58873465/194726873-aa2fbc18-8625-4122-aee9-10370265d9a8.png)



zˆ is the nearest encoding and can be defined as:


![image](https://user-images.githubusercontent.com/58873465/194727117-197a227a-6283-4421-b37c-41ff7d679624.png)



where Lc denotes the context loss whose purpose is to limit the generated image with
respect to the damaged corrupted image y and the mask M. The context loss captures
the remaining available data in the image.
Lp is the prior loss, which has been defined purposefully to punish unrealistic or weird
images.


The term Lc i.e. the context loss can easily be calculated
by getting the l2 norm between the generated image G(z) and the undamaged part of
the input image y as follows.

![image](https://user-images.githubusercontent.com/58873465/194727222-b42227ed-d45e-4c06-9da0-052527c1035d.png)


This approach, however, treats all the pixels in an equal way but for the sake of context
more importance should be given to those pixels that are closest to the damaged por-
tions. This method helps to reduce the significance of pixels that are far away from the
damaged region. To this purpose we define two importance weighing terms as follows:

![image](https://user-images.githubusercontent.com/58873465/194727373-38141f06-9447-453f-8aba-b3b790361d9e.png)


Let W be the weighting term and i be the pixel index. Then the weight term is defined
as:

![image](https://user-images.githubusercontent.com/58873465/194727400-a87b2b80-8f9e-4596-a797-0b8c632959c5.png)


This term is calculated for all values of i for which Mi = 0. For all the is such that
Mi != 0 then Wi = 0. γ is the distance of the pixel to the nearest unknown pixel in the
damaged image. Once the Weight matrix has been obtained, calculation of context loss
Lc is done as follows:

![image](https://user-images.githubusercontent.com/58873465/194727446-67cb3b26-5f5f-48d3-a0ab-bcc99d146fd3.png)


where . represents element-wise multiplication. Here we are taking the l1 norm because it performs slightly better than the l2 norm.


![image](https://user-images.githubusercontent.com/58873465/194727494-1865878a-5fae-4e76-90af-15d48acb863b.png)



This term is calculated for all values of i for which Mi = 0. For all the is such that
Mi != 0 then Wi = 0. γ is the distance of the pixel to the nearest unknown pixel in the
damaged image. So we take the square of the distance and and compute W with it.
Once the Weight matrix has been obtained, calculation of context loss Lc is done as
follows:


![image](https://user-images.githubusercontent.com/58873465/194727528-6dc48108-4b7d-49ad-a085-76e2d374ff84.png)


where . represents element-wise multiplication. Here we are taking the l1 norm because it performs slightly better than the l2 norm.




The model has been evaluated on the CelebFaces Attributes Dataset (CelebA) dataset[16].
This dataset contains a total of 202,599 face images. We remove 500 images from this
dataset to create our test dataset. All of the images are cropped at the centre to dimen-
sions of 64×64.





 
Results:

Without Weighted Context


![image](https://user-images.githubusercontent.com/58873465/194728030-bf6b28e4-a2fc-42c0-b4ce-4c16c2b513dc.png)



![image](https://user-images.githubusercontent.com/58873465/194728125-249cf5e6-c92d-4d09-b53f-12ddfe08ddd7.png)



![image](https://user-images.githubusercontent.com/58873465/194728151-6fcc28e5-3e7c-4a7a-be93-58444c0181ba.png)



![image](https://user-images.githubusercontent.com/58873465/194728289-db5fab85-5fa9-4639-aa49-eb2534738949.png)



![image](https://user-images.githubusercontent.com/58873465/194728337-fa586a40-67f8-4e3a-baf4-a44e67498b13.png)



![image](https://user-images.githubusercontent.com/58873465/194728351-97ed23ad-01c4-496e-9385-17ef3907e548.png)



![image](https://user-images.githubusercontent.com/58873465/194728361-ac65d71a-c7c2-4ea6-a02d-e75e0279ba2f.png)
















