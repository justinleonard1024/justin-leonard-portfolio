/********************************
 * Super Stop N Buy
 * StoreCheckOut.cs
 * Created by Justin Leonard
 * < Other Names Omitted >
********************************/

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Net;
using System.Net.Mail;
using System.ComponentModel.DataAnnotations;
using System.Text.RegularExpressions;

namespace SuperStopNBuy
{
    public partial class StoreCheckOut : Form
    {
        double total;

        protected override void OnFormClosing(FormClosingEventArgs e)
        {
            // Initialize
            base.OnFormClosing(e);
            if (e.CloseReason == CloseReason.WindowsShutDown) return;

            // Open form
            this.Hide();
            DemoMain formDemoMain = new DemoMain();
            formDemoMain.Show();
        }


        public StoreCheckOut()
        {
            InitializeComponent();
        }
        public StoreCheckOut(double passedSum)
        {
            total = passedSum;
            InitializeComponent();
        }

        private void labelLogo_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Checkout will be cancelled");
            this.Hide();
            var formTemp = new StoreMain();
            formTemp.Show();
        }

        private void StoreCheckOut_Load(object sender, EventArgs e)
        {
            labelTotal.Text = "$" + total.ToString($"F{2}");
        }

        private void buttonCheckout_Click(object sender, EventArgs e)
        {
            // Check first name text box
            if (String.IsNullOrEmpty(textBoxFName.Text))
            {
                MessageBox.Show("Please enter a valid first name", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            // Check last name text box
            if (String.IsNullOrEmpty(textBoxLName.Text))
            {
                MessageBox.Show("Please enter a valid last name", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            // Check email text box & email verification was added
            if (String.IsNullOrEmpty(textBoxEmail.Text) || !Regex.IsMatch(textBoxEmail.Text,
                @"^(?("")("".+?(?<!\\)""@)|(([0-9a-z]((\.(?!\.))|[-!#\$%&'\*\+/=\?\^`\{\}\|~\w])*)(?<=[0-9a-z])@))" +
                @"(?(\[)(\[(\d{1,3}\.){3}\d{1,3}\])|(([0-9a-z][-0-9a-z]*[0-9a-z]*\.)+[a-z0-9][\-a-z0-9]{0,22}[a-z0-9]))$",
                RegexOptions.IgnoreCase, TimeSpan.FromMilliseconds(250)))
            {
                MessageBox.Show("Please enter a valid email", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            // Check address text box
            if (String.IsNullOrEmpty(textBoxAddress.Text))
            {
                MessageBox.Show("Please enter a valid address", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            // Check credit card number text box
            if (String.IsNullOrEmpty(textBoxCCN.Text) || textBoxCCN.Text.Length != textBoxCCN.MaxLength)
            {
                MessageBox.Show("Please enter a valid credit card number", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            // Check ccv text box
            if (String.IsNullOrEmpty(textBoxCCV.Text) || textBoxCCV.Text.Length != textBoxCCV.MaxLength)
            {
                MessageBox.Show("Please enter a valid ccv", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            // Check expiration date
            if (String.IsNullOrEmpty(dateTimePicker.Text))
            {
                MessageBox.Show("Please enter a valid expiration date", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            // Check card type combo box
            if (String.IsNullOrEmpty(comboBoxType.Text))
            {
                MessageBox.Show("Please enter a valid card type", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            Random rng = new Random();
            int orderNum = rng.Next(10000, 50001);

            //checks credit card length and number
            if (textBoxCCV.TextLength == 3 && textBoxCCN.TextLength == 16)
            {
                MailMessage mail = new MailMessage();
                SmtpClient SmtpServer = new SmtpClient("smtp.gmail.com");
                mail.From = new MailAddress("csci401ric@gmail.com");
                mail.To.Add(textBoxEmail.Text);
                mail.Subject = "Order Confirmation";
                mail.Body = "Hello " + textBoxFName.Text + ",\n\n Super Stop 'N Buy thanks you for your purchase of $" + total.ToString($"F{2}") + "!\n\nYour Order Confirmation number is: " + orderNum + "\n\nThanks for shopping, visit us again soon!\n\n\nSuper Stop 'n Buy®\n1000 Main Street\nProvidence, RI 02860";

                SmtpServer.Port = 587;
                SmtpServer.Credentials = new System.Net.NetworkCredential("csci401ric@gmail.com", "rhodeisland18");
                SmtpServer.EnableSsl = true;
                SmtpServer.Send(mail);

                MessageBox.Show("Order Placed! Order Number is: " + orderNum + "\nThanks For Shopping at Super Stop 'n Buy!");
                this.Hide();
                var formTemp = new StoreMain();
                formTemp.Show();
            }
            else
            {
                if (textBoxCCV.TextLength != 3)
                {
                    MessageBox.Show("CCV Number Incorrect");
                }
                else
                {
                    MessageBox.Show("Credit Card Number Incorrect");
                }
            }
        }
    }
}
