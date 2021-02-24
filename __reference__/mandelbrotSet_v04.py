#! python 3
# mandelbrotSet.py - f_{c}(z)=z^{2}+c where z=0

import os, logging, math
from PIL import Image, ImageDraw

'-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
# Sets up logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
logging.disable(logging.DEBUG) # uncomment to block debug logging.debug messages
#logging.disable(logging.INFO) # uncomment to block debug logging.info messages and below

'-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
'-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
# This function normalizes data linearly

def normalizeData(inputValue, inputMax, inputMin, nMax=1.0, nMin=0.0):

    Pn = ((inputValue - inputMin)/(inputMax-inputMin)) * (nMax - nMin)+ nMin
    return Pn

'-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
'-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
#converts incoming values into logarithm to with 255(max RGB value) as limit. This will help sperate values in the mid and lower range range

def logConversion(value): # To work properly input (1,1000)
    logBase = 10
    baseMulitplicationDigit = 3 # i.e 10*100 = 1000

    fn = (256*math.log(value,logBase))/baseMulitplicationDigit #f(n)=255logn/6
    #logging.debug('For x=%s: fn=%s' %(value,fn))

    return fn


'-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
'-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------'

def main():

    # Creates Image
    im = Image.new('RGBA', (350,200), 'black')
    draw = ImageDraw.Draw(im)
    logging.info("Created canvas %s pixels by %s" % (im.size[0], im.size[1]))

    # Sets varibales to hold the size of the image.
    # This will be used to normalize the pixel infomation in a valid range for the Madelbort set.
    # Which only accepts X-values between (-2.5, 1.0) and Y-values between (-1.0, 1.0).
    Px_rangeMax = im.size[0]
    Px_rangeMin = 0
    Py_rangeMax = im.size[1]
    Py_rangeMin = 0

    '-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
    #Adjustable variables

    max_iteration = 1000 # Change this value to adjust iteration detail

    # Manipulate the position within mandelbrotSet
    scalerMultiple = 0.004   # Scale(zoom) image. Values between 1.0 and 0.0
    translate_x = -0.7745     # Transform position in x. Negative values shift left <-<- . Positive shift right ->->
    translate_y = -0.1265   # Transform position in y. Negative values shift up. Positive shift down

    # Defines 'c' value. Sets the normalization scale. Use this to control field of view for image.
    # X scale must be between (-2.5, 1.0)
    tX_Max = (1.0 * scalerMultiple) + translate_x
    tX_Min = (-2.5 * scalerMultiple) + translate_x
    # Y scale must be between(-1.0, 1.0)
    tY_Max = (1.0 * scalerMultiple) + translate_y
    tY_Min = (-1.0 * scalerMultiple) + translate_y

    logging.info('x-range:(%s,%s) y-range:(%s,%s)' % (tX_Min, tX_Max, tY_Min, tY_Max))

    # Sets the colorspace
    colorspace = 'log' # Use this value to choose between linear or logarithic colorspace choose either 'lin' or 'log'
    logging.info('Colorspace data in %s' % colorspace)

    '-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
    '-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------'

    logging.info("Drawing image...")
    for Py in range(0,Py_rangeMax):
        for Px in range(0,Px_rangeMax):
            x0= normalizeData(Px+1, Px_rangeMax, Px_rangeMin, tX_Max, tX_Min)
            y0 = normalizeData(Py+1, Py_rangeMax, Py_rangeMin, tY_Max, tY_Min)

            #logging.debug(str(Px) + ', ' + str(Py))
            #logging.debug('  ' + str(x0) + ' ' + str(y0))

            '-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------'

            x = 0.0 # Defines 'z' value for x-coordinate. Do NOT change
            y = 0.0 # Defines 'z' value for y-coordinate.  Do NOT change
            iteration = 0 # Do NOT change

            # Main logic loop for function. Determines if 'c' value (x0,y0) maintain stability. i.e. does NOT go to infinity
            while(x*x+y*y <= 2*2 and iteration < max_iteration):
                xtemp = x*x-y*y +x0
                y = 2*x*y +y0
                x = xtemp
                iteration += 1 #iterate counter


            #logging.debug('\t' + str(round(x,3)) + ' ' + str(round(y,3)) + ' ' + str(iteration) + '\n')

            '-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
            #Define pixel color

            if(colorspace == 'lin'):

                rgbValue_lin = int(normalizeData(iteration,0,max_iteration,0,255)) #interprets the data linearly

                if(iteration < max_iteration*.33): # weight red
                    color = (rgbValue_lin, int(rgbValue_lin/2), int(rgbValue_lin/2))
                elif(iteration >= max_iteration*.33 and iteration < max_iteration*.66): # weight green
                    color = (int(rgbValue_lin/2), rgbValue_lin, int(rgbValue_lin/2))
                elif(iteration >= max_iteration*.66): # weight blue
                    color = (int(rgbValue_lin/2), int(rgbValue_lin/2), rgbValue_lin)
                    
            if(colorspace == 'log'):

                rgbValue_log = int(logConversion(iteration)) # interprets data on a logarithmic scale

                if(iteration < max_iteration*.33): # weight red
                    color = (rgbValue_log, int(rgbValue_log/2), int(rgbValue_log/2))
                elif(iteration >= max_iteration*.33 and iteration < max_iteration*.66): # weight green
                    color = (int(rgbValue_log/2), rgbValue_log, int(rgbValue_log/2))
                elif(iteration >= max_iteration*.66): # weight blue
                    color = (int(rgbValue_log/2), int(rgbValue_log/2), rgbValue_log)

            draw.point((Px,Py), color) #plot point

    logging.info('Done drawing!')


    '-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
    # Outputting Image

    # sets the current working directory to the location of the script
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # Defines file pathing
    versionNum = 'v010'
    resolution = str(Px_rangeMax) + 'by' + str(Py_rangeMax)
    fileName = 'madelbrotSet_%s_%s.png' % (resolution, versionNum)
    filePath = os.path.join(dname , 'images\\rawRenders')

    # Creates final output image
    logging.info('Saving canvas as %s\\%s' % (filePath,fileName))
    '''
    im.save(os.path.join(filePath, fileName))
    '''
    #function END
    logging.info('DONE: program complete')
    return 0


'-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
'-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------'

if __name__ == "__main__":
    main()
