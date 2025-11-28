import os
from lxml import etree
import subprocess

# --- Configuration ---
XML_FILE = 'cdcatalog.xml'
XSLT_FILE = 'cdcatalog.xsl'
XSL_FO_FILE = 'document.fo'
#OUTPUT_PDF_FILE = 'formatted_output.pdf'
OUTPUT_PDF_FILE = "formatted_output.pdf"

#C:\xml\TEST_XSL\fo_cdcatalog_fo.xsl

current_working_directory = os.getcwd()
# print output to the console
print(current_working_directory)

# Adjust this path to your FOP installation
FOP_PATH = r"C:\xml\Apache_FOP\fop-2.11\fop\fop.bat" 

def transform_xml_to_fo(xml_path, xslt_path, output_fo_path):
    """Step 1: Uses lxml to transform XML data into an XSL-FO document."""
    print("Step 1: Transforming XML to XSL-FO...")
    try:
        # Load the source XML and XSLT stylesheet
        xml_doc = etree.parse(xml_path)
        xslt_doc = etree.parse(xslt_path)
        
        # Create the XSLT transformer
        transformer = etree.XSLT(xslt_doc)
        
        # Apply the transformation
        fo_result = transformer(xml_doc)
        
        # Save the result (the XSL-FO file)
        fo_result.write(output_fo_path, pretty_print=True, encoding='utf-8')
        print(f"Successfully generated XSL-FO file: {output_fo_path}")
        return True
    except etree.XSLTApplyError as e:
        print(f"XSLT Transformation Error: {e}")
        return False
    except FileNotFoundError:
        print("Error: XML or XSLT file not found.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred during XSLT: {e}")
        return False

def render_fo_to_pdf(fo_path, pdf_path, fop_executable):
    """Step 2: Calls the Apache FOP processor to render the XSL-FO document to PDF."""
    print("\nStep 2: Rendering XSL-FO to PDF using FOP...")
    
    # Construct the FOP command
    command = [fop_executable,'-d', '-fo', fo_path, '-pdf', pdf_path] # -d :))
    
    try:
        # Execute the command and capture output
        result = subprocess.run(
            command,
            check=False,  # Raises an exception for non-zero exit codes (errors) if TRUE!!!!
            capture_output=True,
            text=True
        )
        ####
        exit_code = result.returncode
        print("--- FOP STDOUT (Output) ---")
        print(result.stdout)

        print("--- FOP STDERR (Errors/Warnings) ---")
        print(result.stderr)
        print("\n--- FOP Execution Results ---")
        print(f"Exit Code: {exit_code}")
        ####
        print(f"Successfully generated PDF: {pdf_path}")
        
    except subprocess.CalledProcessError as e:
        print("FOP Rendering Error:")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
        print("Ensure Java is correctly installed and FOP is configured.")
    except FileNotFoundError:
        print(f"Error: FOP executable not found at {fop_executable}. Check your FOP_PATH.")
    except Exception as e:
        print(f"An unexpected error occurred during FOP execution: {e}")


# --- Main Execution ---
if __name__ == "__main__":
    
    # Run Step 1: XML -> XSL-FO
    success = transform_xml_to_fo(XML_FILE, XSLT_FILE, XSL_FO_FILE)

    if success:
        # Run Step 2: XSL-FO -> PDF
        render_fo_to_pdf(XSL_FO_FILE, OUTPUT_PDF_FILE, FOP_PATH)
        print('printed successfully')
        print(XSL_FO_FILE)
        # Cleanup (Optional)
        # os.remove(XSL_FO_FILE)
        # print(f"\nCleaned up intermediate file: {XSL_FO_FILE}")